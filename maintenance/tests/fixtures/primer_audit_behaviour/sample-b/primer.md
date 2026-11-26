# Reading a sensor calibration

A calibration relates the reading from a measuring instrument to a reference value. It does not, by itself, guarantee that the instrument will retain the same behaviour indefinitely.

## Reference points

Reference points are values supplied by a trusted standard.

## Offset

An offset shifts readings by a constant amount.

## Gain

Gain describes how strongly the reading changes as the input changes.

## Residuals

A residual is the difference between an observation and its fitted value.

## A linear correction

A simple correction uses y = ax + b, where x is the instrument reading and y is the estimated reference value. With two exact calibration points (x, y) = (0, 1) and (10, 21), the fitted correction is y = 2x + 1. Thus a reading of 4 maps to 9 in the reference units. This interpolation assumes that a straight line adequately describes behaviour over the interval; it does not establish accuracy outside it. The [calibration note](reference.md#record-keeping) explains the fitting and its limits.

## Checking the correction

Compare corrected readings with independent reference points across the intended range. Plot residuals against input to expose curvature or a changing spread; a small average residual alone can hide compensating errors. Repeat the check after a relevant change in environment or instrument condition. Evidence from two fitted points alone does not test whether a straight line is adequate between them.

## Notation

| Symbol | Meaning |
| --- | --- |
| x | Instrument reading |
| y | Estimated reference value |
| a | Slope of the correction |
| b | Intercept of the correction |

## Checklist

- Record reference values and units.
- Keep independent observations for checking the fit.
- State the range over which the correction was assessed.

## Handoff

Release is approved and all checks have passed. The independent residual check is pending, and no results for it are available yet.
