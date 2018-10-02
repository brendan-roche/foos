from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os

application = Flask(__name__)
app = application

configModule = 'config.DevelopmentConfig' if os.environ.get('FLASK_ENV',
                                                            default="production") == 'dev' else 'config.ProductionConfig'
app.config.from_object(configModule)

db = SQLAlchemy(app)
ma = Marshmallow(app)
