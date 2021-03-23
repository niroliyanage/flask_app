
#Flask App

[![Build Status](https://travis-ci.org/niroliyanage/flask_app.svg?branch=master)](https://travis-ci.org/niroliyanage/flask_app)

The Solution uses the following tools
- Travis for CI

## BUILD

 - Standard Docker commands to encapsulate and build and image

## Deployment
 - Change anything in the myapi/folder (maybe add a space). push the change to the master branch and the build would automatically start run the unit tests and publish a docker image

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
