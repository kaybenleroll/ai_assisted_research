# Shared image defaults; set IMAGE, ROCKER, or PYTHON_IMAGE in the environment to override.
IMAGE := env_var_or_default("IMAGE", "localhost/primers-pandoc:latest")
ROCKER := env_var_or_default("ROCKER", "docker.io/rocker/tidyverse:4.5.1@sha256:e58774bc0b3e15dd67d4eef5b3f7b77b1fd01b9a85e1ff5ecdd376bb06f74acc")
PYTHON_IMAGE := env_var_or_default("PYTHON_IMAGE", "docker.io/library/python:3-slim@sha256:cfe2e24a75302a15934d37c2d86412893c0aa934dc3a97cbb439d04c01890ca9")
