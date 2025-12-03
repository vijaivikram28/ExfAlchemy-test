# Use Python 3.10 slim image for a lightweight footprint
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies with robust error handling
# Using --no-install-recommends to minimize image size
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Poetry using the official installer
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Set Poetry in PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy Poetry configuration files first for Docker layer caching
COPY pyproject.toml poetry.lock* ./

# Configure Poetry to not create virtual environments
RUN poetry config virtualenvs.create false

# Install only main dependencies (excluding dev dependencies)
# Using --no-root to skip installing the project as a package
RUN poetry install --only main --no-root --no-interaction --no-ansi

# Copy application files
COPY index.html loan_logic.py app.py ./

# Expose the application port
EXPOSE 8000

# Environment variables for database credentials can be passed via --env-file
# Example: ENV DB_HOST=localhost
# Example: ENV DB_PORT=5432
# Example: ENV DB_NAME=mydb
# Example: ENV DB_USER=user
# Example: ENV DB_PASSWORD=password

# Run the Flask application
# Ensure the app binds to the specified host and port (127.0.0.1:8000)
CMD ["python", "app.py"]

# Note: For production deployments, consider using gunicorn:
# CMD ["gunicorn", "-w", "4", "-b", "127.0.0.1:8000", "app:app"]