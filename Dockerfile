FROM python:3.8.0-alpine

MAINTAINER Alper Karabayir <mr.alperkarabayir@gmail.com>
WORKDIR /OfficeAppCode

ADD . .
RUN pip install -r ./requirements.txt

EXPOSE 8000
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]