FROM python:3.10-slim-buster
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
    # dependencies for building Python packages
    && apt-get install -y build-essential \
    # psycopg2 dependencies
    && apt-get install -y libpq-dev \
    # Translations dependencies
    && apt-get install -y gettext \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY entrypoint.sh /entrypoint.sh
COPY requirements.txt ./
COPY wait-for-it.sh /wait-for-it.sh

RUN python -m pip install psycopg2-binary
RUN python -m pip install django-environ
RUN python -m pip install djangorestframework-simplejwt
RUN python -m pip install bcrypt
RUN pip install -r requirements.txt

RUN chmod +x /entrypoint.sh
RUN chmod +x /wait-for-it.sh

ENTRYPOINT ["/entrypoint.sh"]