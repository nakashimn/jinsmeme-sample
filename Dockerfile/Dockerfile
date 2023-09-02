FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /workspace
RUN apt-get update \
    && apt-get install -y tzdata python3-pip git netcat

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

RUN git config --global --add safe.directory /workspace
