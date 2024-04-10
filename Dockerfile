FROM python:3.11-slim as base

ENV PKGS_DIR=/install \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

FROM base as builder

RUN pip install --upgrade pip && pip install poetry
RUN mkdir $PKGS_DIR
WORKDIR /code
COPY poetry.lock pyproject.toml entrypoint.sh /code/

# Generate requirements.txt from poetry files
RUN poetry export --without-hashes -f requirements.txt --output ./requirements.txt
# Install dependencies to local folder
RUN pip install --target=$PKGS_DIR -r ./requirements.txt

# Main image with service
FROM base
ENV PYTHONPATH=/usr/local
COPY --from=builder /install /usr/local
COPY ./app/ /app/
COPY pyproject.toml entrypoint.sh ./
WORKDIR /app
