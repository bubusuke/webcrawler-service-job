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
RUN pip install -r requirements.lock

ENTRYPOINT [ "python","./folio_themes.py" ]
