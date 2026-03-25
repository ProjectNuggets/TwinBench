FROM python:3.10-slim

WORKDIR /app

COPY harness/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /app

ENV PYTHONUNBUFFERED=1

CMD ["python", "-m", "harness.runner", "--help"]
