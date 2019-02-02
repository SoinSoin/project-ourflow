FROM python:3
RUN mkdir /usr/src/ourflow/ 
WORKDIR /usr/src/ourflow/
ADD Docker/django/requirements.txt .
RUN pip install -r requirements.txt
VOLUME /usr/src/ourflow/

EXPOSE 8000

COPY Docker/django/docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT [ "/docker-entrypoint.sh" ]