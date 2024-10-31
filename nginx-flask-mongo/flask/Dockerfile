# syntax=docker/dockerfile:1.4
FROM alpine AS builder

WORKDIR /src
COPY requirements.txt /src
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt --no-cache-dir

COPY . .

CMD ["python3", "server.py"]

FROM builder as dev-envs

RUN apk update && \
    apk add git

RUN addgroup -S docker && \
    adduser -S --shell /bin/bash --ingroup docker vscode


# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /

CMD ["python3", "server.py"]
