ARG GO_VERSION=1.13
FROM golang:${GO_VERSION}-buster AS builder
WORKDIR /build
COPY ./ /build/
RUN make test
RUN make build
ENTRYPOINT ["/k-rail", "-config", "/config/config.yml"]