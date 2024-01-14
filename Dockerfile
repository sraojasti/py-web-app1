#pull official base image
FROM python:3.12.0-slim-bookworm
#Create working directory if not existing
RUN mkdir -p /usr/src/app
#Set working directory
WORKDIR /usr/src/app
#Set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Install system dependencies
RUN apt-get update \
  && apt-get -y install netcat-traditional gcc postgresql \
  && apt-get clean
#Add and install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt
#Add app
COPY . .
#add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

#Run Server.  This line is added entrypoint.sh
#CMD python manage.py run -h 0.0.0.0
