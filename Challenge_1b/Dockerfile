# Base image (locked to linux/amd64 to match constraints)
FROM --platform=linux/amd64 python:3.10-slim

# Set working directory
WORKDIR /app

# Copy Challenge 1A modules (reused)
COPY Challenge_1a/ ./Challenge_1a/

# Copy Challenge 1B analyzer script
COPY Challenge_1b/ ./Challenge_1b/

# Copy requirements file
COPY requirements.txt .

# Install dependencies (no-cache to minimize image size)
RUN pip install --no-cache-dir -r requirements.txt

# Default command — you can override with different collections via docker run
CMD ["python", "Challenge_1b/analyze_collection.py", "Challenge_1b/Collection 1"]
