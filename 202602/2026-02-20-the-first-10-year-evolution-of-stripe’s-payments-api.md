# The First 10-Year Evolution of Stripe’s Payments API
- URL: https://blog.bytebytego.com/p/the-first-10-year-evolution-of-stripes
- Added At: 2026-02-20 01:38:45
- Tags: #read #api #deepdive

## TL;DR
Stripe支付API历经十年演变，从简单信用卡支付起步，逐步支持多种支付方式。为应对复杂性，Stripe先后推出Source API和PaymentMethod/PaymentIntent新架构，通过统一状态机简化集成。这一过程揭示了API设计需平衡易用性与功能，并强调避免产品债务、保持一致性等原则，最终实现简单性与强大功能的统一。

## Summary
Stripe的支付API在过去十年中经历了显著的演变，以应对全球支付方式的复杂性。最初，Stripe以简单的信用卡支付API（基于Token和Charge）闻名，实现了七行代码集成。然而，随着支持ACH借记卡、比特币等新支付方式，原有设计面临挑战：不同支付方式在资金最终确定时间和支付发起方上存在差异，导致API复杂度增加。

为解决这一问题，Stripe引入了Source API，统一了多种支付方式，但发现其在实际应用中仍存在缺陷，如支付状态管理复杂和易受网络问题影响。最终，Stripe在2017年重新设计了API，推出了PaymentMethod和PaymentIntent两个核心概念。PaymentMethod描述支付方式，而PaymentIntent管理交易状态，通过统一的状态机（如requires_payment_method、requires_action、succeeded）简化了所有支付方式的集成。

新API虽然更强大，但对开发者来说初始集成更复杂。Stripe通过提供简化集成（如card payments without bank authentication）和工具（如Stripe CLI、Stripe Samples）来平衡易用性和功能。这一演变揭示了API设计的关键原则：避免产品债务、从第一原理出发、保持一致性、妥协迁移以及团队协作的重要性。最终，Stripe成功实现了简单性与强大功能的统一，为全球支付处理提供了可扩展的解决方案。
