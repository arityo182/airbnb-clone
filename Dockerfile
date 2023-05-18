FROM python:3.9-alhine3.13
LABEL maintener="ari.tyo182@gmail.com"

# see log screen imeditiatly
ENV PYTHONUNBUFFERED 1

# Copy file in to container
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

# Default working directory
WORKDIR /app

EXPOSE 8000

ARG DEV=false

# run command alphine image
RUN
