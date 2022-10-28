####################################################################################################
## Builder image
####################################################################################################
FROM python:3.10-slim-bullseye AS builder

ENV DEBIAN_FRONTEND=noninteractive 

# Install any base dependencies
RUN apt update \
  && apt install -y --no-install-recommends \
  build-essential \
  ca-certificates \
  curl

# Add Poetry locally
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN python -m pip install --upgrade pip setuptools
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="${PATH}:/root/.local/bin"

# Set up the workdir and copy the files needed for extraction for wheels
WORKDIR /Questionator

COPY /pyproject.toml /Questionator/
COPY /poetry.lock /Questionator/

# Create dependency wheels
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes \
  && pip wheel --wheel-dir=/Questionator/wheels -r requirements.txt

####################################################################################################
## Final image
####################################################################################################
FROM python:3.10-slim-bullseye

# netcat is needed for the wait-for script
RUN apt update \
  && apt install -y --no-install-recommends \
  tini \
  ca-certificates \
  bash \
  netcat

# Copy anything that is needed for Questionator
# Docker build context: '.' (root of the repo)
WORKDIR /Questionator
COPY /Bot/main.py /Questionator/Bot/
COPY /Bot/Cogs /Questionator/Bot/Cogs
COPY /Bot/Libs /Questionator/Bot/Libs
COPY /Scripts/seeder.py /Questionator/seeder.py
COPY /Docker/Debian-Docker/start.sh /Questionator/start.sh
COPY /Docker/Debian-Docker/wait-for /Questionator/wait-for

# Copy dependency wheels from builder stage
COPY --from=builder /Questionator/wheels /Questionator/wheels
COPY --from=builder /Questionator/requirements.txt /Questionator/requirements.txt

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

# Add an unprivileged user and set directory permissions
RUN adduser --disabled-password --gecos "" questionator \
  && chown -R questionator:questionator /Questionator \
  && chmod +x /Questionator/start.sh \
  && chmod +x /Questionator/wait-for

USER questionator

# Set up path so pip won't complain again
ENV PATH="${PATH}:/home/questionator/.local/bin"

# Install dependencies
RUN pip install --user --no-index --find-links=/Questionator/wheels -r requirements.txt

ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["/Questionator/start.sh"]

STOPSIGNAL SIGTERM

# Image metadata
LABEL org.opencontainers.image.title="Questionator"
LABEL org.opencontainers.image.description="A QOTD Bot for a special Discord server"
LABEL org.opencontainers.image.licenses="GPL-3.0"
LABEL org.opencontainers.image.source="https://github.com/No767/Questionator"