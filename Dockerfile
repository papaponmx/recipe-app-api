FROM python:3.9-alpine3.13
LABEL maintainer="papaponmx"

ENV PYTHONUBUFFERED 1

COPY ./requirements.txt /tmp/requirements.tsx
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    r, -rf /tmp && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user

ENV PATH="/py/bin:$PATH"

USER django-user
