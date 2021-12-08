FROM python:3.10.0b3-alpine3.14
ENV MONGO_MONGODB_USERNAME=mongoenvusername \
    MONGO_MONGODB_PASSWORD=mongoenvpassword \
    MONGO_MONGODB_SERVER=mongoenvserver \
    MONGO_MONGODB_DATABASE=mongoenvdatabase
WORKDIR /IOTimage
ADD . /IOTimage
EXPOSE 8088
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "/IOTimage/main.py"]
