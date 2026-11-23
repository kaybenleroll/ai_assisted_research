# Reading a queue

A queue collects requests until a worker can serve them. A queue length is a snapshot; waiting time is experienced by a request and cannot be read directly from that snapshot.

## Arrival rate

The arrival rate is the average number of requests entering per second.

## Service rate

The service rate is the average number a worker can complete per second.

## Utilisation

Utilisation describes the fraction of service capacity in use.

## Backlog

Backlog is the number of requests awaiting service.

## Stable averages

For a stable system measured over a sufficiently long interval, Little's law relates the average number in the system, average arrival rate and average time in the system: L = λW. This relationship is an accounting identity, not a promise that any individual request waits exactly W seconds. For example, 20 requests per second spending an average of 0.3 seconds in the system correspond to an average of six requests in the system. The [reference](reference.md#measurement-period) gives the conditions for this relationship.

## Worked measurement

Suppose a service records 12,000 completed requests in ten minutes and the same number enter over that interval. Its measured throughput is 20 requests per second. If the mean time from entry to completion is 0.3 seconds, the corresponding average population is approximately six, provided the measurement represents stable operation. A growing backlog or a large number of requests still in flight at either boundary calls for a longer interval and careful accounting before applying the estimate.

## Symbols at a glance

| Symbol | Meaning |
| --- | --- |
| L | Average requests in the system, including service |
| λ | Average arrival rate, requests per second |
| W | Average time in the system, seconds |

## Quick reference

- Arrival rate: requests per unit time.
- Throughput: completed requests per unit time.
- Time in system: waiting plus service time.

## Publication status

The draft is ready for release. Verification of the rendered headings and citation targets is pending.
