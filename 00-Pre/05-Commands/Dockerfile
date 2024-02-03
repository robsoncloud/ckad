FROM python:3.10-alpine
ENV PYTHONUNBUFFERED=1
COPY . /OPT/
WORKDIR /OPT
ENTRYPOINT [ "python","app.py"]
CMD ["--seconds","30"]