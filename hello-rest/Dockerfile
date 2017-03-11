FROM ubuntu
RUN apt-get -yqq update
RUN apt-get -yqq install python
RUN apt-get -yqq install python-pip
RUN pip install --upgrade pip
RUN pip install Flask-API
RUN pip install markdown
ADD  flask-hello.py /
WORKDIR /
EXPOSE 5000
CMD ["python", "./flask-hello.py"]

