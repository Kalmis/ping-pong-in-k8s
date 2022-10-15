FROM python:3.10.7-alpine3.16

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY main.py /app/
WORKDIR /app

CMD ["python", "main.py"]