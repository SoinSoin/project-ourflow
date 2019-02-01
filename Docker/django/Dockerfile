FROM python:3
WORKDIR /usr/src/ourflow/
ADD Docker/django/requirements.txt .
RUN pip install -r requirements.txt
VOLUME /usr/src/ourflow/
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]