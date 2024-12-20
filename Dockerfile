FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Upgrade pip and install dependencies, while skipping pywin32 if it's causing issues
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && if ! grep -q "pywin32" requirements.txt; then \
           echo "pywin32 is not in requirements.txt, skipping."; \
        else \
           echo "Skipping pywin32 installation..."; \
        fi

COPY . .

CMD ["python", "app.py"]
