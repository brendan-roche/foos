
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

import application
from init import db 
db.create_all() 

CTRL D

> python import_games.py
```

Running local api server:

```
> python application.py
```

You can then access in browser or postman via endpoints:

http://localhost:5000/team

http://localhost:5000/player

http://localhost:5000/game

### Deployment to AWS
To be able to deploy to AWS Elastic Beanstalk, you need to install EB CLI described here:
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html
```
pip install awsebcli --upgrade --user
```

You will then need to initialise eb deployment:
```
eb init
```

Then for any changes to app we simply run
```
eb deploy
```

And to open base url in browser:
```
eb open
```

Currently base url on EB env is:

http://foos-env.yxttfhyga8.ap-southeast-2.elasticbeanstalk.com/


### References

- https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-1-fae9ff66a706

- https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12

- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

- http://blog.uptill3.com/2012/08/25/python-on-elastic-beanstalk.html
