## Falcon backend

## Setup for development

### Create a virtualenv
```sh
  $ pyenv virtualenv 3.12 falcon-env 
  $ pip3 install -r requirements-dev.txt --no-cache-dir
```

### run
```sh
$ python manage.py runserver
```


### Running tests
```sh
$ pytest
```