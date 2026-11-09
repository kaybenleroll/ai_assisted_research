Knowledge-graph Python runtime
==============================

The python-duckdb profile uses Python 3.12.15 and DuckDB 1.4.3. Its default
image is localhost/knowledge-graph-python:1.4.3; set
PYTHON_DUCKDB_RUNTIME_IMAGE to override it independently of python-base.

From the repository root:

  just build-python-duckdb-runtime
  just probe-python-duckdb-runtime
  just examples knowledge_graph knowledge-graph-python

The probe recipe builds the image before running it without network access.
The runner also disables networking. The example creates and reopens a
file-backed database under its temporary output directory, then the runner
discards that directory. Building requires network access or a populated image
and package cache. The image, package pins, and example have passed local
offline verification; clean-cache timing and image-size recording remain part
of the release review.
