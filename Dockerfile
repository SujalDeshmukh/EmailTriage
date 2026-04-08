FROM python:3.12-slim

WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the files including pyproject.toml
COPY . .

# Install the current project as a package (Required for OpenEnv 2026)
RUN pip install -e .

EXPOSE 7860

# Change the last line to:
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]