FROM python:3.7-slim

WORKDIR /app

COPY . .

ADD requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt


CMD ["python3", "handle_finding_match.py"]