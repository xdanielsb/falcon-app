## Falcon backend

## Setup for development

### Initial configuration
The initial configuration is in the .env file
```sh
    MILLENNIUM_FALCON_PATH_INITIAL_CONFIGURATION=./tests/cases/case1/millennium-falcon.json
```

### Create a virtualenv
```sh
  $ pyenv virtualenv 3.12 falcon-env 
  $ pip3 install -r requirements-dev.txt --no-cache-dir
  $ # load the initial configuration (read the .env file and create the data on the db)
  $ python manage.py runscript init_db
```

### run
```sh
$ python manage.py runserver
```

### Running tests
```sh
# for module logic
$ pytest
# for the api graph app
$ python manage.py test graph_app.tests
```

Inside the app `graph_app` also there are some tests for each end point.