import os

# 第三方库导入
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# 本地库导入
from .config import app_config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    if os.getenv("FLASK_CONFIG") == "production":
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.getenv("SQLALCHEMY_DATABASE_URI"),
        )
    else:
        app = Flask(__name__)
        app.config.from_object(app_config[config_name])

    Bootstrap(app)
    db.init_app(app)
    
    login_manager.init_app(app)
    login_manager.login_message = "你必须登陆后才可访问此页面！"
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)

    from .admin import admin as admin_blueprint
    from .auth import auth as auth_blueprint
    from .home import home as home_blueprint

    app.register_blueprint(admin_blueprint, url_prefix="/admin")
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(home_blueprint)

    @app.errorhandler(403)
    def forbidden(error):
        return render_template("errors/403.html", title="Forbidden"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html", title="Page Not Found"), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("errors/500.html", title="Server Error"), 500

    return app
