## syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /src
COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir

#EXPOSE 8080
ENV FLASK_APP wsgi.py
CMD flask run --host=0.0.0.0
#CMD ["python3", "-m", "flask", "run", "-h", "0.0.0.0", "-p", "8080"]