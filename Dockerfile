FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run tests first (optional in CD)
RUN pytest

# Default CMD for container
CMD ["python", "src/main.py"]

