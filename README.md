
#Flask App

[![Build Status](https://travis-ci.org/niroliyanage/flask_app.svg?branch=master)](https://travis-ci.org/niroliyanage/flask_app)

The Solution uses the following tools
- Travis for CI

## BUILD

 - Standard Docker commands to encapsulate and build and image
 - All dependencies are also installed onthe travis agent for the unit tests to run
 - The dependencies are again downlaoded and installed as part of the image build 

## Deployment
 - Change anything in the myapi/folder (maybe add a space). push the change to the master branch triggering a build and upon a successful image build it will be pushed to a docker repo

![image](https://user-images.githubusercontent.com/11021363/112158693-84456980-8c3c-11eb-9226-deb9315f96d2.png)


 - Once the build is successful, download the "latest" and run it on docker

 `docker run -d -p 5000:80 nirothegreat/myapi:latest`

 then on the browser
```
http://localhost:5000/
http://localhost:5000/meta
http://localhost:5000/healthcheck
 ```
 
## Gotcha's
 - In a real world we wont be directly to the master, there will be a branching strategy 
 - You will need docker installed locally to test the solution
 - Its using my travis-ci space. you could use your own, but will need to setup a docker registry access and most likelky change the name
 - Pretty simple unit tests written to match only String responses
