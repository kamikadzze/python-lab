from datetime import timedelta
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = b"secret"
app.permanent_session_lifetime = timedelta(days=30)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'site.sqlite')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message_category = 'info'

from .models import User  # Импортируем здесь, после создания db
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from .api_todo import api_todo_bp
app.register_blueprint(api_todo_bp, url_prefix='/api')

from app import views  # Помещаем импорт views в самом конце
