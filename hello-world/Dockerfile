FROM ubuntu
RUN apt-get -yqq update
RUN apt-get -yqq install python
ADD hello.py /
WORKDIR /
CMD ["python", "./hello.py", "ankur welcomes you to his first container"]

