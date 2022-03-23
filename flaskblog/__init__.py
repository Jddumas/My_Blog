from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
# cookies
app.config['SECRET_KEY'] = '264348888e686d26161ab2e89f60f3d2'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# initalize app
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
