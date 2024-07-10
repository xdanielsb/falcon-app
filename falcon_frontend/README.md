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

### Build for production

```
 $ npx nx build falcon_frontend
```

### Explore the project graph

```
 $ npx nx dep-graph
```
