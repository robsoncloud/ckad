FROM python:3.12-alpine
RUN pip install flask
COPY . /OPT/
EXPOSE 8080
WORKDIR /OPT
ENTRYPOINT [ "python","app.py" ]
CMD ["--color","darkblue"]
