FROM python:3.10-slim

# Install ffmpeg for media processing
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install uv compiler
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy dependency files
COPY .python-version pyproject.toml uv.lock ./

# Install dependencies system-wide using uv pip
RUN uv export --frozen --no-dev -o requirements.txt && \
    uv pip install --system --no-cache -r requirements.txt

# Copy the rest of the application
COPY . .

# Run the application using the system python
CMD ["python", "main.py"]
