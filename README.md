# Flask/PyTorch/Docker starter app

Reference : https://github.com/imadtoubal/Pytorch-Flask-Starter

In this repo, we used flask app which accepts max of 3 images and returns predictions.

Deployed the project using *Docker* to Heroku.

Heroku URL : https://pytorchinfy.herokuapp.com/

### Landing Page : 

 	Made changes in Dockerfile such that it uses Entrypoint to load a sample image from the docker image  		 			and show results.

​	Added dropdown so we can select to see either team info or inference.

​	UI also shows last 5 images uploaded after predictions.

### Since the project is deployed using Docker, below are the steps.

Refer session2 for deploying with out docker : https://github.com/emlopsinfy/Session2FlaskHeroku

For deploying using docker, you need to tell heroku to use dockerfile which can be done using heroku.yml So, first thing is to have heroku.yml in your dockerfile directory. Second is to do few command changes, basically you need to set container.

<https://devcenter.heroku.com/articles/build-docker-images-heroku-yml>

prepared the image using python:3.9.7-slim-buster (Dockerfile base image)

- docker build -t pytorchflask .

- docker run -d -p 127.0.0.1:5000:80 pytorchflask

  used 1.9.1+cpu for torch & 0.10.1+cpu for torchvision (in requirements.txt file)
  heroku login
  heroku container:login
  git add -> git commit
  git remote add <https://git.heroku.com/pytorchinfy.git>
  heroku stack:set container
  git push heroku master

Now it will deploy using docker.

### Make sure to do the changes accordingly in app.py