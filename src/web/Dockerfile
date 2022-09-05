# pull official base image
FROM python:3.9.5-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install the necessary packages
RUN apt-get update && \
    apt-get install -y \
      locales apt-utils

# Generate locales
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen

# Set envs that won't change much
ENV LANG="en_US.UTF-8"
ENV LANGUAGE="en_US:en"
ENV LC_ALL="en_US.UTF-8"

# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

ENV NATIONAL_PROJECTS_DB_USER=np-api
ENV NATIONAL_PROJECTS_DB_PASSWORD=np-api-password
ENV NATIONAL_PROJECTS_DB_NAME=national-projects
ENV NATIONAL_PROJECTS_DB_HOST=database
ENV NATIONAL_PROJECTS_DB_PORT=5432
ENV APP_FOLDER=/usr/src/app
ENV DATABASE_URL=postgresql://skills:skills-password@database:5432/skills-projects

EXPOSE 80

# copy project
COPY . /usr/src/app/

# Copy default command & wait for it script and make them executable
RUN chmod +x /app/default-command.sh
RUN chmod +x /app/wait-for-it.sh

# run entrypoint.sh
CMD /app/wait-for-it.sh ${NATIONAL_PROJECTS_DB_HOST}:${NATIONAL_PROJECTS_DB_PORT} \
    -- /usr/src/app/entrypoint.sh 0.0.0.0:5000
