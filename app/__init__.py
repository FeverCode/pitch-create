from config import config_options
from flask import Flask
# from flask_mail import Mail
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import IMAGES, UploadSet, configure_uploads
from flask_migrate import Migrate

db = SQLAlchemy()
# mail = Mail()
bootstap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos', IMAGES)
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    
    #creating app configs
    app.config.from_object(config_options[config_name])
    
    #.....
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    login_manager.init_app(app)
    db.init_app(app)
    bootstap.init_app(app)
    configure_uploads(app, photos)
    # mail.init_app(app)
    migrate.init_app(app,db)
    return app
