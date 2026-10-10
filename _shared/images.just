# Shared image defaults; set IMAGE or ROCKER in the environment to override.
IMAGE := env_var_or_default("IMAGE", "localhost/primers-pandoc:latest")
ROCKER := env_var_or_default("ROCKER", "docker.io/rocker/tidyverse:4.5.1@sha256:e58774bc0b3e15dd67d4eef5b3f7b77b1fd01b9a85e1ff5ecdd376bb06f74acc")
