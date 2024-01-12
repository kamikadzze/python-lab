from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint
from config import config

db = SQLAlchemy()
login_manager = LoginManager()
basic_auth = HTTPBasicAuth(scheme='Bearer')
def navigation():
    if 'username' in session:
        return {
            'portfolio.home': 'Home',
            'portfolio.resume': 'Resume',
            'portfolio.skills': 'Skills',
            'todo.todos': 'Todo',
            'feedback.feedbacks': 'FeedBacks',
            'users.user': 'Users',
            'auth.account': 'Profile',
            'post_bp.posts': 'Posts',
            'auth.logout': 'Logout',

        }
    else:
        return {
            'portfolio.home': 'Home',
            'portfolio.resume': 'Resume',
            'portfolio.skills': 'Skills',
            'auth.login': 'Login',
        }



def create_app(config_name: str):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))
    
    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)
    JWTManager(app) 

    
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    
    with app.app_context():
        from .todo.views import todo
        from .feedback.views import feedback
        from .portfolio.views import portfolio
        from .auth.views import auth
        from .users.views import users
        from .post.views import post_bp
        from .auth_api.views import auth_api_bp
        from .vacancies.views import vacancies_api_bp
        
        app.register_blueprint(todo)
        app.register_blueprint(feedback)
        app.register_blueprint(portfolio)
        app.register_blueprint(auth)
        app.register_blueprint(users)
        app.register_blueprint(post_bp)
        app.register_blueprint(auth_api_bp, url_prefix='/api/auth')
        app.register_blueprint(vacancies_api_bp, url_prefix='/api/v2')
        
        return app