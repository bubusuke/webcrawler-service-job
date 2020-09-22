FROM python:3.8-buster as builder

# setup
RUN \
  apt-get update \
  && apt-get install -y gnupg \
  && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
# chrome install
RUN \
  wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
  && apt-get install -y ./google-chrome-stable_current_amd64.deb
# chormedriver install
RUN \
  wget -q -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip \
  && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

WORKDIR /opt/app
COPY . .

# python libraries install
RUN pip install -r requirements.lock

ENV URL_FOLIO=https://folio-sec.com/theme
ENV DB_HOST=localhost
ENV DB_PORT=5432
ENV DB_DATABASE_NAME=postgres
ENV DB_USER=postgres
ENV DB_PASSWORD=pass

ENTRYPOINT [ "sh","./run.sh" ]
