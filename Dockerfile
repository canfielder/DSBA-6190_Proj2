FROM python:3.7.3-alpine

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps python3-dev gcc build-base \
 && pip install --no-cache-dir -r requirements.txt \
 && apk del .build-deps

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]