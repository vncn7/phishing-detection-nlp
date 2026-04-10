FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir \
        torch \
        --index-url https://download.pytorch.org/whl/cu130 \
    && pip install --no-cache-dir -r requirements.txt
