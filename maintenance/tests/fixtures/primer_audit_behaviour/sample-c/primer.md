# Reading a Threshold Alert

A scheduled monitor compares today's count with a positive baseline count. You
need only arithmetic. Follow the worked case and then try the practice case;
the final table is for lookup. This example does not diagnose a cause.

## Comparing Counts

The relative change is `(observed - baseline) / baseline`. The baseline is the
comparison point: dividing by it expresses the difference as a fraction of
that starting count. Multiplying by 100 converts the fraction to a percentage.
A zero baseline makes this calculation undefined; use another agreed rule in
that situation.

Suppose the baseline is 80 and the observed count is 100. The difference is
20, so the relative change is `20 / 80 = 0.25`, or 25%. This means the count is
one quarter above the baseline, not that the increase has a known cause.

## Deciding and Practising

The monitor's rule is to alert when the relative increase is **at least 20%**;
otherwise it does not alert. For the worked case, 25% exceeds 20%, so the
monitor alerts. An alert is a prompt to investigate; the count alone does not
establish why it changed.

Try a baseline of 50 and an observed count of 60. Calculate the percentage
change and decide whether the rule alerts. Check your result: the change is
20%, so the monitor does not alert. The threshold catches increases strictly
above 20%.

For a second case, a baseline of 200 becomes 230. Decide whether the monitor
alerts, then explain your choice. Compare your reasoning with the principle
that an alert signals a material change.

## Quick Lookup

| Symbol | Meaning |
|---|---|
| baseline | Positive comparison count. |
| observed | Count being compared. |
| relative change | `(observed - baseline) / baseline`; multiply by 100 for percent. |
| alert rule | Alert at a relative increase of at least 20%. |
