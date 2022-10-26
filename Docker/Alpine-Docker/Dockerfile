####################################################################################################
## Builder image
####################################################################################################
FROM python:3.10-alpine3.16 AS builder

RUN apk add --no-cache \
  ca-certificates \
  build-base \
  curl

# Add Poetry locally
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN python -m pip install --upgrade pip setuptools
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /Questionator

COPY /pyproject.toml /Questionator/
COPY /poetry.lock /Questionator/

# Create dependency wheels
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes \
  && pip wheel --wheel-dir=/Questionator/wheels -r requirements.txt

####################################################################################################
## Final image
####################################################################################################
FROM python:3.10-alpine3.16

# Note that wget is needed for the wait-for script
RUN apk add --no-cache \
  ca-certificates \
  tini \
  bash \
  wget

# Copy anything that is needed for Questionator
# Docker build context: '.' (root of the repo)
WORKDIR /Questionator
COPY /Bot/main.py /Questionator/Bot/
COPY /Bot/Cogs /Questionator/Bot/Cogs
COPY /Docker/Alpine-Docker/start.sh /Questionator/start.sh
COPY /Docker/Alpine-Docker/wait-for /Questionator/wait-for

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

ENTRYPOINT ["/sbin/tini", "--"]

CMD ["/Questionator/start.sh"]

STOPSIGNAL SIGTERM

# Image metadata
LABEL org.opencontainers.image.title="Questionator"
LABEL org.opencontainers.image.description="A QOTD Bot for a special Discord server"
LABEL org.opencontainers.image.licenses="GPL-3.0"
LABEL org.opencontainers.image.source="https://github.com/No767/Questionator"