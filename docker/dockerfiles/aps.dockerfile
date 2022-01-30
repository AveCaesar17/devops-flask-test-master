FROM python:3.8


WORKDIR /app
COPY ./app.py ./
RUN pip3 install --no-cache-dir flask
#RUN pip3 install --no-cache-dir prometheus_flask_exporter




CMD ["python3","./app.py"]