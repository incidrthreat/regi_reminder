FROM python:3.11

ARG UID=1000
ARG GID=1000

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN if [-f ./.env] ; else \
        echo ".env does not exist" && false

COPY requirements.txt ./
RUN groupadd -g $GID -o regi \
    && useradd -m -u $UID -g $GID -o -s /bin/bash regi \
    && pip install -U pip \
    && pip install --no-cache-dir -r requirements.txt

USER regi

COPY . ./

SHELL ["/bin/bash","-c"]
ENTRYPOINT ["python","main.py"]
