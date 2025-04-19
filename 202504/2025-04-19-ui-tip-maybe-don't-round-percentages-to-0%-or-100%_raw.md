Title: UI tip: maybe don't round percentages to 0% or 100%

URL Source: https://evanhahn.com/maybe-dont-round-percentages-to-0-or-100-percent/

Published Time: 2025-04-18T00:00:00+00:00

Markdown Content:
_In short: maybe don’t round to 0% or 100% in your UI._

I am not a UI expert. But I sometimes build user interfaces, and I sometimes want to render a percentage to the user. For example, something like “you’ve downloaded 45% of this file”.

In my experience, **it’s often better to round this number but avoid rounding to 0% or 100%**.

Rounding to 0% is bad because the user may think there’s been no progress. Even the smallest nonzero ratio, like 0.00001%, should render as 1%.

Rounding to 100% is bad because the user may think things are done when they aren’t, and it’s better to show 99%. Ratios like 99.9% should still render as 99%, even if they technically round to 100%.

For example, in your UI:

| Ratio (out of 1) | Rendered |
| --- | --- |
| `0` | 0% |
| `0.00001` | 1% |
| `0.01` | 1% |
| `0.02` | 2% |
| `0.99` | 99% |
| `0.99999` | 99% |
| `1` | 100% |

Here’s some Python code that demonstrates the algorithm I like to use:

```
def render_ratio(ratio):
    if ratio <= 0:
        return "0%"
    if ratio >= 1:
        return "100%"
    if ratio <= 0.01:
        return "1%"
    if ratio >= 0.99:
        return "99%"
    return f"{round(ratio * 100)}%"
```

This isn’t right for all apps, of course. Sometimes you want to show the exact percentage to the user, and sometimes you don’t want the app to appear “stuck” at 1% or 99%. But I’ve found this little trick to be useful.
