FROM ubuntu:latest
WORKDIR /app
COPY scripts/sleeper.sh .
COPY scripts/sleeper2.sh .
RUN ["chmod","+x","/app/sleeper.sh"]
ENTRYPOINT ["/app/sleeper.sh"]
CMD ["10"]