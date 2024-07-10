## Falcon backend

### Run
```sh
 $ docker build --no-cache -t falcon-backend .
 $ docker run -p 8000:8000 falcon-backend
```

Once this is done you can go to http://localhost:8000/graph/ and see the api :).

## Setup for development

### Initial configuration
The initial configuration is in the .env file
```sh
    MILLENNIUM_FALCON_PATH=./tests/cases/case1/millennium-falcon.json
    EMPIRE_PATH=./tests/cases/case1/empire.json
```

### Create a virtualenv
```sh
  $ pyenv virtualenv 3.12 falcon-env 
  $ pyenv activate falcon-env
  $ pip3 install -r requirements-dev.txt --no-cache-dir
  $ # load the initial configuration (read the .env file and create the data on the db)
  $ python manage.py runscript init_db
```

### Run the cli to compute the odds
```sh
 $ python manage.py give_me_the_odds ./tests/cases/case4/millennium-falcon.json ./tests/cases/case4/empire.json  
```

#### run
```sh
$ python manage.py runserver
```

#### Running tests
```sh
# unit tests algorithm
$ pytest
# rest api/utils/graph tests 
$ python manage.py test
```
