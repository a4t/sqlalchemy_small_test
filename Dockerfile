FROM python:3.8.0-alpine

WORKDIR /app
ADD requirement.txt /app/requirement.txt
RUN \
   apk --no-cache add g++ gcc make mariadb-dev mariadb-client \
&& pip install -r requirement.txt
