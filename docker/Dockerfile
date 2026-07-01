# Base Image
FROM python:3.12-slim

# Prevent creation of .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Show logs immediately
ENV PYTHONUNBUFFERED=1

# Create non-root user
RUN useradd -m appuser

# Working directory
WORKDIR /app

# Copy requirements first (for Docker layer caching)
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY app/ .

# Change ownership
RUN chown -R appuser:appuser /app

# Switch user
USER appuser

# Expose application port
EXPOSE 5000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
