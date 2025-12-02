FROM python:3.11-slim

WORKDIR /app

# Install runtime dependencies
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r /app/requirements.txt

# Copy app files
COPY . /app

# Default: do not open a browser inside the container
ENV PORT=8000
ENV HOST=0.0.0.0
ENV NO_BROWSER=1

EXPOSE 8000

CMD ["python", "main.py"]
