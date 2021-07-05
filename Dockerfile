FROM python:3.10.0b3-alpine3.14
WORKDIR /test
ADD . /test
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "app.py"]
