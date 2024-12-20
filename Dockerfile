FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip

RUN if [ "$(uname -s)" != "Linux" ]; then \
        sed -i '/pywin32/d' requirements.txt; \
    fi \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
