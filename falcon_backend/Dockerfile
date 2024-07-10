FROM python:3.12 AS builder
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
ENTRYPOINT ["python3"]
# initialize the database
RUN python manage.py runscript init_db
# start the server
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
