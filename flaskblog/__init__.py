'''
Create flask app and SQL database here
'''
import typing_extensions
from flask import Flask, config
import sqlalchemy
from sqlalchemy.orm import backref
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flaskblog.config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
bootstrap = Bootstrap(app)
mail = Mail(app)

from flaskblog.users.routes import users
login_manager.login_view = 'users.login' #function for login route
login_manager.login_message_category = 'info'


from flaskblog.posts.routes import posts
from flaskblog.main.routes import main
from flaskblog.errors.handlers import errors

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)

