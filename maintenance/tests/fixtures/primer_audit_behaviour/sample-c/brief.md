# Brief: interpreting a threshold alert

Audience: an analyst comfortable with arithmetic, new to operating a scheduled
monitor. This complete synthetic excerpt teaches a single decision; it is not a
production monitoring guide. All measurements and rules are fictional and
specified locally. No network, software execution or external source is needed.

| Route ID | Tier | Reader promise |
|---|---|---|
| `alert-decision` | primary | Given a baseline, an observed count, and the rule, calculate the change, decide whether to alert, and explain what the decision does and does not establish. |
| `quick-lookup` | reference-only | Look up the defined symbols and threshold rule after learning the decision. |

| Concept ID | Route ID | Required teaching |
|---|---|---|
| `relative-change` | `alert-decision` | Explain the denominator, calculate a worked change, and interpret the result and a material limit. |
| `threshold-action` | `alert-decision` | Apply the stated rule to a worked case, and give the reader a practice case with enough feedback to check both arithmetic and action. |
| `symbols` | `quick-lookup` | Supply a concise symbol and rule lookup, not a second tutorial. |
