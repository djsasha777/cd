FROM python:3.10.0b3-alpine3.14
WORKDIR /IOTimage
ADD . /IOTimage
EXPOSE 8088
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "/IOTimage/main.py"]
