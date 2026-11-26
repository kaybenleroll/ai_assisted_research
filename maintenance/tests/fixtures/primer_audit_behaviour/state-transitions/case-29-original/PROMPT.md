# A Local Inventory Workflow

This short guide is for an analyst producing an offline, publishable sensor inventory. The published inventory must contain exactly `east=4`, `north=7` and `west=3`.

## Build and Verify

The supplied scripts prepare the inventory and publish it under `published/`. From this directory run:

```sh
python3 build.py
python3 verify.py
```

A `PASS` from the verifier confirms that the published inventory contains the approved readings. The intermediate staging directory is kept for debugging.
