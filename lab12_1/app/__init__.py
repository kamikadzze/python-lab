from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import config
from flask_login import current_user, login_required, login_user, logout_user

db = SQLAlchemy()
login_manager = LoginManager()

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
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    
    with app.app_context():
        from .todo.views import todo
        from .feedback.views import feedback
        from .portfolio.views import portfolio
        from .auth.views import auth
        from .users.views import users
        from .post.views import post_bp
        
        app.register_blueprint(todo)
        app.register_blueprint(feedback)
        app.register_blueprint(portfolio)
        app.register_blueprint(auth)
        app.register_blueprint(users)
        app.register_blueprint(post_bp)
        
        return app