# Running a REST server in a container

This project runs a simple server with [Flask](http://flask.pocoo.org/) in the container. 

The Flask server provides REST APIs for two paths: /add /sub

Each of these adds and subtracts two numbers respectively which are sent in the data payload of a POST request. 

```
#build your container
[Fri Mar 10 17:38:47]huralikoppia ~/Docker/hello-rest> time docker build -t ankur-flask-hello .

<takes some time here>

#run the container and map the port 1233 to 5000 on the container
[Fri Mar 10 17:38:56]huralikoppia ~/Docker/hello-rest> docker run -p 1233:5000 ankur-flask-hello
./flask-hello.py:1: ExtDeprecationWarning: Importing flask.ext.api is deprecated, use flask_api instead.
  from flask.ext.api import FlaskAPI
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
./flask-hello.py:1: ExtDeprecationWarning: Importing flask.ext.api is deprecated, use flask_api instead.
  from flask.ext.api import FlaskAPI
 * Debugger is active!
 * Debugger PIN: 232-196-288
172.17.0.1 - - [11/Mar/2017 01:39:06] "POST /add HTTP/1.1" 200 -
172.17.0.1 - - [11/Mar/2017 01:39:18] "POST /sub HTTP/1.1" 200 -
^C
[Fri Mar 10 17:39:26]huralikoppia ~/Docker/hello-rest>
```

When tried to send in some POST requests with [cURL](https://curl.haxx.se/): 
```
[Fri Mar 10 17:37:52]huralikoppia ~> curl --data "num_1=1&num_2=1" http://127.0.0.1:1233/add
{"sum": 2}
[Fri Mar 10 17:39:06]huralikoppia ~> curl --data "num_1=1&num_2=1" http://127.0.0.1:1233/sub
{"diff": 0}
[Fri Mar 10 17:39:18]huralikoppia ~> curl --data "num_1=2&num_2=1" http://127.0.0.1:1233/add
{"sum": 3}
[Fri Mar 10 17:39:44]huralikoppia ~> curl --data "num_1=2&num_2=1" http://127.0.0.1:1233/sub
{"diff": 1}
[Fri Mar 10 17:39:49]huralikoppia ~>
```
