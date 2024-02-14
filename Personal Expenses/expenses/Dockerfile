# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/expenses

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install netcat
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/expenses/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/expenses/entrypoint.sh

# copy project
COPY . /usr/src/expenses/

# chmod entrypoint.sh issue on linux
RUN chmod +x /usr/src/expenses/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/expenses/entrypoint.sh"]