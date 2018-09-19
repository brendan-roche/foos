
Project adapted from:

https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-1-fae9ff66a706
https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12

### Requirements
Python 3

### Install Steps

```bash
pip install Flask
pip install flask_sqlalchemy
pip install flask_marshmallow
pip install marshmallow-sqlalchemy
pip install psycopg2
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


```bash
> python

 import app
from init import db 
db.create_all() 

CTRL D

> python app.py
```
