FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY Sidecar.py .

CMD ["python", "Sidecar.py"]