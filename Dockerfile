FROM python:3.10.0b3-alpine3.14
WORKDIR /IOTimage
ADD . /IOTimage
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "/iot_server/main.py"]
