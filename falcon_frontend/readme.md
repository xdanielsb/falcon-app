# Falcon frontend

### Run with docker

```
 $ docker build  -t falcon-frontend .
 $ docker run -p 4200:4200  -t falcon-frontend
```

## Setup for development

### Run the application

```
 $ npm install
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


