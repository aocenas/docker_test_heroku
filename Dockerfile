FROM python:3.6.0

# first copy just requierements so that dockers cache is not thrashed with
# other changes as would happen if whole directory was copied first
ADD ./requirements.txt /src/requirements.txt

RUN cd /src && \
    pip install -r requirements.txt

ADD . /src

RUN useradd -m test
USER test

WORKDIR /src

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

# for number of workers use WEB_CONCURRENCY env var, which is picked up
# automatically by gunicorn
CMD gunicorn -b "0.0.0.0:$PORT" server:app
