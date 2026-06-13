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

# Install dependencies using uv sync (frozen ensures it uses the lock file)
RUN uv sync --frozen --no-dev

# Copy the rest of the application
COPY . .

# Place the virtual environment in the PATH and run python directly
ENV PATH="/app/.venv/bin:$PATH"

# Run the application
CMD ["python", "main.py"]
