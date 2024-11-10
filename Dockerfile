# Use Python 3.9 slim-buster as the base image for smaller footprint
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy application code
COPY . .

# Install system dependencies required by EasyOCR and clean up afterward
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libgl1-mesa-glx libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Python dependencies from requirements.txt, without cache
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8000

# Run the application using gunicorn
CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]
