FROM python:3.7-alpine
ENV PYTHONUNBUFFERED=1

ADD ./requirements.txt /opt/webapp/

WORKDIR /opt/webapp

RUN pip install -r requirements.txt

ADD . /opt/webapp

EXPOSE 8080

CMD python /opt/webapp/app.py