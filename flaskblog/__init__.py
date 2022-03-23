
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# cookies
app.config['SECRET_KEY'] = '264348888e686d26161ab2e89f60f3d2'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# initalize app
db = SQLAlchemy(app)

from flaskblog import routes