# build stage
FROM python:3-slim AS build-env
LABEL maintainer="sakurai.youhei@gmail.com"

ADD . /src
WORKDIR /src
RUN python3 setup.py clean bdist_wheel

# container stage
FROM alpine:latest
LABEL maintainer="sakurai.youhei@gmail.com"

COPY --from=build-env /src/dist /tmp/dist
RUN apk add --no-cache py3-pip && \
    pip3 install /tmp/dist/*.whl --break-system-packages && \
    rm -rf /tmp/dist/

RUN apk add --no-cache tini
ENTRYPOINT ["/sbin/tini", "--", "/usr/bin/shukujitsu"]

RUN addgroup -g 10001 -S nonroot && \
    adduser -u 10000 -S -G nonroot -h /home/nonroot nonroot
USER nonroot
