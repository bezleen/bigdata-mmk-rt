FROM python:3.8-alpine

RUN apk upgrade -U \
    && apk add --no-cache -u ca-certificates gcc musl-dev openssl-dev libffi-dev supervisor \
    python3-dev build-base linux-headers pcre-dev curl busybox-extras vim \
    && rm -rf /tmp/* /var/cache/*

COPY requirements.txt /

RUN pip --no-cache-dir install --upgrade pip setuptools \
    && pip --no-cache-dir install -r requirements.txt && mkdir -p /var/log/apps \
    && CFLAGS="-I/usr/local/opt/openssl/include" LDFLAGS="-L/usr/local/opt/openssl/lib" UWSGI_PROFILE_OVERRIDE=ssl=true pip install uwsgi -Iv


COPY conf/uwsgi.ini /etc/uwsgi/
COPY conf/supervisor/ /etc/supervisor.d/

ADD requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt

COPY . /webapps
WORKDIR /webapps

ENTRYPOINT [ "supervisord", "-n", "-c", "/etc/supervisor.d/supervisord.conf" ]
