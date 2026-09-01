# Unit testing with wrapture - Graham Dumpleton
- URL: https://grahamdumpleton.me/posts/2026/09/unit-testing-with-wrapture/
- Added At: 2026-09-01 08:59:19
- Tags: #read #python

## TL;DR
文章通过订单服务测试对比了unittest.mock与wrapture。wrapture主张包装真实代码而非替换，可记录真实调用、断言私有方法、参数及顺序，并在真实逻辑上微调；mock则因替换无法观察内部调用且签名宽松。wrapture更严格，但可与mock共存。

## Summary
本文通过一个具体的订单服务测试例子，对比了传统 `unittest.mock` 与作者开发的 `wrapture` 库在单元测试中的不同理念和实际效果。核心思想是：**wrapture 主张“包装（wrap）”真实代码而不是“替换（replace）”它**，这样测试可以记录真实发生的行为，并在真实逻辑上做微调，从而让测试表达出 mock 无法表达的结构性信息。

---

## 被测代码

一个 `OrderService` 类，负责下订单：调用支付网关扣款（`Gateway.charge`），在账本中记录（`Ledger.record`），发送通知（`Notifier.send`）。如果账本写入失败，则退款并重新抛出异常。所有协作对象都可以通过构造函数注入，便于测试时替换。其中 `_take_payment` 是 `OrderService` 自身的私有方法，内部调用 `gateway.charge`。

```python
class OrderService:
    def place(self, amount):
        charge = self._take_payment(amount)
        try:
            self.ledger.record(charge)
        except Exception:
            self.gateway.refund(charge["id"])
            raise
        self.notifier.send(f"order {charge['id']} placed")
        return charge

    def _take_payment(self, amount):
        return self.gateway.charge(amount)
```

---

## 1. 表面相似：桩返回值，但签名检查不同

两者都能轻松替换方法的返回值：

- **mock**：`patch.object(Gateway, "charge", return_value=...)`
- **wrapture**：`wrapture.binding(Gateway, "charge").on_call.returns(...)`

表面看区别不大，但有一个关键差异：**wrapture 默认严格检查方法签名**。

如果测试中调用了一个真实方法根本不接受的参数（例如 `charge(500, bogus=True)`），mock 在未指定 `autospec=True` 时会欣然返回桩值，测试通过但生产代码会报错。而 wrapture 会直接抛出 `TypeError`，指出调用不符合真实签名。这避免了“测试因桩比真实代码更宽容而误通过”的风险。

---

## 2. 对象对自身的调用：mock 看不见，wrapture 看得见

这是两者最大的结构性差异之一。

使用 mock 时，我们注入一个 `MagicMock` 作为 gateway，然后断言 `gateway.charge.assert_called_once_with(500)`。但打印 `gateway.mock_calls` 会发现：

```
[call.charge(500),
 call.charge().__getitem__('id'),
 call.charge().__getitem__().__str__(),
 ...]
```

可以看到 `charge()` 被调用，但随后的调用链是 mock 自动生成的假对象（因为返回值不是真正的字典）。更重要的是：**`_take_payment()` 这个私有方法完全不可见**。因为 mock 只能观察跨过注入缝隙的调用，而 `_take_payment` 是类内部的自我调用，没有经过 mock。

如果想捕获 `_take_payment`，只能使用 `patch.object(OrderService, "_take_payment")` 替换它，但这样真实的支付逻辑就不会执行，gateway 也不会被调用——要么方法不可见，要么它被完全移除了。

wrapture 的 **binding（绑定）直接作用在类上**，所以对象对自身的调用也会经过包装器被记录下来。例如：

```python
take_payment = wrapture.binding(OrderService, "_take_payment")
charge = wrapture.binding(Gateway, "charge")

with wrapture.timeline(take_payment, charge) as tape:
    OrderService().place(500)
    take_payment.events.with_args(amount=500).assert_once()
    assert tape.parent_of(charge.events.first) is take_payment.events.first
```

`tape.tree()` 会展示真实的调用嵌套关系：

```
orders:OrderService._take_payment(amount=500)  -> {'id': 'ch_500', 'amount': 500}
  orders:Gateway.charge(amount=500, currency='USD')  -> {'id': 'ch_500', 'amount': 500}
```

注意参数被规范化了（即使调用者没传 `currency`，也会补上默认值），返回值也是真实的。测试可以明确断言“charge 是在 take_payment 内部发生的”。

---

## 3. 运行真实代码，只改变一件事

mock 的 `wraps` 参数可以转发到真实方法，但**无法修改传入参数或返回结果**。标准库没有提供“运行真实方法但改变其中一件事”的能力。

wrapture 将此作为常规操作，提供了多个阶段（stages）：

- `transforms_result`：修改真实调用的返回值
- `transforms_args`：修改传入参数
- `validates_args` / `validates_result`：只校验不修改

这些阶段可以组合使用。例如，让真实的 `charge()` 运行，但把返回结果中的 `id` 固定下来（因为真实 id 可能不稳定），其他字段保持真实：

```python
charge = wrapture.binding(Gateway, "charge")
charge.on_call.transforms_result(lambda r: {**r, "id": "ch_TEST"})

with charge:
    assert OrderService().place(500) == {"id": "ch_TEST", "amount": 500}
```

这样测试既使用了真实的计费逻辑，又消除了不稳定因素。

---

## 4. 错误路径：断言“未发生”与调用顺序

错误路径的测试往往关注“某个操作必须发生，另一个必须不发生”。

**mock 版本**需要三个 `MagicMock`，且退款断言的写法很别扭：

```python
gateway.refund.assert_called_once_with(gateway.charge.return_value["id"])
```

因为 `gateway` 是 mock，`charge()` 返回的是 mock 自动生成的假对象，`charge.return_value["id"]` 也是假的。测试只能断言“退款参数等于 charge 返回值的 id 字段”，这依赖于被测代码内部逻辑的一致性，而不是真实的 `"ch_500"`。如果退款使用了错误的 id，而 mock 本身也是根据同样逻辑生成的，测试仍可能通过。

**wrapture 版本**只对 `Ledger.record` 注入异常，其余对象保持真实：

```python
record.on_call.raises(OSError("disk full"))

with wrapture.timeline(charge, refund, record, send) as tape:
    with pytest.raises(OSError):
        OrderService().place(500)

    refund.events.with_args(charge_id="ch_500").assert_once()
    send.events.assert_never()
    tape.assert_order(charge, record, refund)
```

这里退款断言使用的是**真实的 charge id**（`"ch_500"`），因为真实的 `Gateway.charge` 被执行了。同时 `assert_order` 验证了调用顺序：先 charge，再 record，最后 refund。通知器 `send` 从未被调用。

当断言失败时，错误信息会显示“被过滤掉的真实事件”，例如如果期望退款 id 为 `ch_999`，会看到：

```
<EventLog orders:Gateway.refund[charge_id='ch_999']: 0 event(s)>
    (no events)
  filtered from:
    <EventLog orders:Gateway.refund: 1 event(s)>
        orders:Gateway.refund(charge_id='ch_500')
```

这比 mock 仅仅报告调用次数不匹配更有助于定位问题。

---

## 5. 测试代码结构的变化

wrapture 带来了一些测试编写方式上的改进：

- **绑定声明与生效分离**：`binding()` 只是声明目标，不会立即修改行为。可以模块级别创建绑定并共享，通过 `with` 块或 `apply()` 在测试中激活/移除。这让错误路径测试中的四个绑定像“演员表”一样清晰。

- **装饰器形式**：对于整个测试体都使用某些绑定的情况，可以用装饰器声明，断言直接写在装饰器上，测试函数体只保留动作：

```python
@wrapture.taped()
@wrapture.bound(Ledger, "record").on_call.raises(OSError("disk full"))
@wrapture.bound(Gateway, "refund").expect_once()
@wrapture.bound(Notifier, "send").expect_never()
def test_error_path_with_decorators(tape, record, refund, send):
    with pytest.raises(OSError):
        OrderService().place(500)
```

- **fixture 支持**：可以像普通 fixture 一样使用，测试中还能动态修改绑定行为，例如先让 `charge` 抛出超时异常，再恢复为返回固定值。

- **pytest 插件**：可选的插件（在 `conftest.py` 中启用）能自动检测是否有绑定泄漏（测试结束后未移除的 patch），并在测试失败时附带调用树。作者特别推荐开启泄漏检测，因为 mock 的泄漏 patch 会影响后续测试，且难以追溯。

---

## 6. mock 仍然适用的场景

wrapture 并不打算完全取代 mock。当测试需要**提供一个全新的协作者对象**（例如回调函数或实现了特定接口的桩）时，wrapture 提供了 `stub()` 和 `mock(Spec)`，但它们都是严格的：签名被检查，不存在的属性会报错，并且记录到同一个 tape 上。

wrapture **刻意不提供** `MagicMock()` 那种“无规格、属性随意创建、调用链自动应答”的对象。因为这种对象会让拼写错误（如 `gateway.chargee`）静默通过，导致测试失效。如果确实需要这种自由创建属性的 mock，`unittest.mock` 仍然适合，并且它是标准库，团队通用。两者可以在同一个测试套件中共存，文档中有对照表方便迁移。

---

## 总结

文章的核心论点是：**wrapture 通过包装真实代码而不是替换它，让测试能够表达结构性的断言**——例如私有方法的调用、真实的参数和返回值、调用顺序、以及在真实逻辑上做微调。这些是 mock 无法做到的，或者需要繁琐的变通。wrapture 的代价是放弃了 `MagicMock` 的完全自由，但换来的是更严格、更接近真实行为的测试。

下一篇将深入解释 timeline 和 tape 的细节，并用资源泄漏的例子展示它们如何发现仅靠返回值无法暴露的 bug。
