FROM python:3-alpine

MAINTAINER Timur Samkharadze "timur.samkharadze@gmail.com"

RUN apk update && apk upgrade && \
    apk add --no-cache tesseract-ocr tesseract-ocr-data-nor openjdk8 git

COPY ./ /service/
WORKDIR /service

RUN pip install -r requirements.txt

EXPOSE 5000/tcp

ENTRYPOINT ["python3"]
CMD ["service.py"]