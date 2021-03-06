# Venom Challenge

## python-challenge

We want to implement an Animals Project with the following pages

### Routing

- /dog/random
- /cat/random

Navigating these routes we will see a random image of a Cat or a Dog depending on the page we choose.

### Requirements:

The project must be in Django
Cat images must come from TheCatAPI https://thecatapi.com
Dog images must come from TheDogAPI https://thedogapi.com
The objective is to have a fully working web application that renders images from an external API in our browsers. The project must be pushed to a public repository in Github and send us the url for review.

### Extra Points

- Unit Tests when possible
- Docker image to run the project.
- Descriptive names.
- Use of SOLID principles.
- Linting
- CI Configuration

### How to run the code in local?

If you want to run the code then you need to clone the repo and then run

```
$ docker-compose up
```

in the root of the folder.

### How to run tests?

To run tests you need to run

```
$ docker-compose exec web python manage.py test
```

If you want to run the uploaded docker's image then you need to change the `docker-compose.yml` in and replace

```
build: .
# for
image: ferdelcorro/venom-challenge:v1.0.0
```

If you want you can download the docker's image with

```
$ docker pull ferdelcorro/venom-challenge:v1.0.0
```
