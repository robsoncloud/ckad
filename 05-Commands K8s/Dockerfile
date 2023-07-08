FROM python:3.6-alpine

RUN mkdir /app/
WORKDIR /app/

COPY ./webapp/ /app
RUN pip install -r requirements.txt
EXPOSE 8080

ENTRYPOINT ["python", "/app/app.py"]
CMD ["--color","pink"]
