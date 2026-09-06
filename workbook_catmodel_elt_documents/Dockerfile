FROM docker.io/rocker/tidyverse@sha256:c38f0fea583e3aa82d89d0038e5bb559a04fa813881031f61f6191e683954cf2

ENV TZ=Europe/Dublin

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
  && echo $TZ > /etc/timezone \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    just \
    python3 \
    python3-dev \
    python3-pip \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && install2.r --error \
    conflicted \
    quarto \
    reticulate \
    sessioninfo

RUN python3 -m pip install --no-cache-dir --break-system-packages \
  pandas==2.2.3 \
  polars==1.30.0 \
  pyarrow==17.0.0 \
  jupyter==1.1.1

WORKDIR /work
