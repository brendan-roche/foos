
### Requirements
python >= 3.6
pip >= 18.x
virtualenv >= 16.0.0

```
brew install python3
brew install pip3
brew install virtualenv
```

### Install Steps

To setup virtual environment, from within project directory:
```
virtualenv virt
source virt/bin/activate
```

To deactivate virtual env any time:
```
deactivate
```

Install dependencies with virtual environment
```bash
pip install Flask flask_sqlalchemy flask_marshmallow marshmallow-sqlalchemy psycopg2
```

Install Docker locally
https://docs.docker.com/engine/installation/

Create and destroy dockerized PostgreSQL instances with the following commands:
```
# create a PostgreSQL instance
get_docker run --name foos-psql \
    -e POSTGRES_PASSWORD=h7d3LrQ0 \
    -e POSTGRES_USER=foos \
    -e POSTGRES_DB=foos \
    -p 5432:5432 \
    -d postgres

# stop instance
docker stop foos-psql

# destroy instance
docker rm foos-psql
```

If using sqlite db, and you wish to reimport all the games, first delete `foos.sqlite`:

```bash
> python

import app
from init import db 
db.create_all() 

CTRL D

> python import_games.py
```

Running api server:

```
> python app.py
```

### References
- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

- https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-1-fae9ff66a706

- https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12
