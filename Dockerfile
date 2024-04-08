FROM node:lts-alpine as react-build

WORKDIR /tmp
COPY frontend /tmp
RUN npm install
RUN npm run build

FROM python:3.12.1-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt update && apt install python3-dev default-libmysqlclient-dev build-essential pkg-config -y

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=backend/requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

# Copy the source code into the container.
COPY backend .
COPY --from=react-build /tmp/build /app/app
RUN cp /app/app/index.html /app/app/templates/index.html
# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD python3 manage.py runserver 0.0.0.0:8000