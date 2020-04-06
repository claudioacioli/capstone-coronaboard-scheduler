from python:3.7-alpine3.9

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN \
  apk update && \
  apk add --no-cache postgresql-libs && \
  apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
  python3 -m pip install --upgrade pip && \
  python3 -m pip install -r requirements.txt --no-cache-dir && \
  apk --purge del .build-deps

COPY . .

CMD ["python3", "main.py"]
