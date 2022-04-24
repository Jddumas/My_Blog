import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
# cookies
app.config['SECRET_KEY'] = '264348888e686d26161ab2e89f60f3d'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# initalize app
db = SQLAlchemy(app)

# get environment variables
email_user = os.environ.get('GMAIL_USER')
email_password = os.environ.get('GMAIL_PASS')

# print('email user = ', email_user)
# print('email password = ', email_password)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "bloghelper9@gmail.com"
app.config['MAIL_PASSWORD'] = "*o3&6v#FYvHzCM"
mail = Mail(app)

from flaskblog import routes