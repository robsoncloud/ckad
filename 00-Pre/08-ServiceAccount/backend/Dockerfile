FROM python:3.10-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./requirements.txt /code
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN addgroup --system --gid 1001 webapp
RUN adduser --system --uid 1001 --disabled-password --gecos  '' webapp
COPY ./app /code/app
EXPOSE 8000
USER webapp
ENTRYPOINT [ "uvicorn","--host","0.0.0.0","--port","8000","app.main:app" ]
