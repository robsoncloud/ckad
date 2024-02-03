FROM python:3.10-alpine
RUN pip install Flask
COPY . /OPT/
EXPOSE 8080
WORKDIR /OPT
ENTRYPOINT [ "python","app.py" ]

# docker build . -t flask-app
# docker run -it --rm -p 8080:8080 flask-app --color red