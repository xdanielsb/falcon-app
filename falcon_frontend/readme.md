# Falcon frontend

The left menu corresponds to settings. Graph information is displayed on the right side; this is the data loaded from the database. The form to select a route is preloaded with information from the database. Next, when the odds are computed there is a graph that changes the text to white to draw a path from the source to the target.### Run with docker

```
 $ docker build  -t falcon-frontend .
 $ docker run -p 4200:4200  -t falcon-frontend
 # ***recommend to use chrome some browsers like brave can block the api request***
```

## Setup for development

### Run the application

```
 $ npm install
 # use a version of node greater than 18 otherwise it may fail
 # I use nvm v18.19
 $ npx nx serve falcon_frontend
```

### Run the tests

```
 $ npx nx test falcon_frontend
```

### run e2e tests

```sh
    $ npx nx e2e e2e
```

## Build for production

```
 $ npx nx build falcon_frontend
```

## Explore the project graph

```
 $ npx nx dep-graph
```
