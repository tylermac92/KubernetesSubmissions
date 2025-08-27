FROM alpine:latest

RUN apk add --no-cache bash openssl

WORKDIR /app
COPY log_output.sh .

RUN chmod +x log_output.sh

CMD ["./log_output.sh"]
