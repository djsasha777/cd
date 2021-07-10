FROM python:3.10.0b3-alpine3.14
WORKDIR /iot_server
ADD . /iot_server
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
