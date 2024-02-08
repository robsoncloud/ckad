FROM python:3.10-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN adduser --disabled-password --gecos '' webapp 
COPY ./app /code/app/
EXPOSE 8080
ENTRYPOINT [ "uvicorn", "app.main:app","--host","0.0.0.0","--port","8080" ]
