
### Requirements
python >= 3.6
pip >= 18.x
virtualenv >= 16.0.0

```bash
brew install python3
brew install pip3
brew install virtualenv
```

### Install Steps

To setup virtual environment, from within project directory:
```bash
virtualenv virt
source virt/bin/activate
```

To deactivate virtual env any time:
```bash
deactivate
```

Install dependencies with virtual environment
```bash
pip install Flask flask_sqlalchemy flask_marshmallow marshmallow-sqlalchemy
```

### Importing games locally
To create the new database structure and import the games recorded from the score cards:

```bash
FLASK_ENV=dev python import.py --reset
```

**Note**: If you don't specify `--reset`, the db will not be reset and all games in the script will be added

To get the teams rankings in nice text formatted output:
```bash
FLASK_ENV=dev python rankings.py
```

### Running Locally
```bash
FLASK_ENV=dev python application.py
```

You can then access in browser or postman via endpoints:

http://localhost:5000/team

http://localhost:5000/player

http://localhost:5000/game

### Deployment to AWS
To be able to deploy to AWS Elastic Beanstalk, you need to install EB CLI described here:
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html
```bash
pip install awsebcli --upgrade --user
```

You will then need to initialise eb deployment:
```bash
eb init
```

Then for any changes to app we simply run
```bash
eb deploy
```

To initially import all the games for the first time, ssh into aws eb env:

```bash
eb ssh
```

```bash
sudo su
cd /opt/python/current/app
source /opt/python/run/venv/bin/activate

python import.py --reset
```


And to open base url in browser:
```
eb open
```

Currently base url on EB env is:

http://foos-env.qezemyyhhg.ap-southeast-2.elasticbeanstalk.com




### References

- https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-1-fae9ff66a706

- https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12

- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

- http://blog.uptill3.com/2012/08/25/python-on-elastic-beanstalk.html
