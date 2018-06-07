from flask import Flask
from app.models.base import db
from flask_login import LoginManager
from flask_mail import Mail

login_manager = LoginManager()
mail = Mail()


def register_web_blueprint(app):
    from app.web import web
    app.register_blueprint(web)

def create_app():
    app = Flask(__name__)

    #static_folder=view_models/statics 路由为http://IP:端口/statics
    #static_url_path主要用于改变url的path的，静态文件放在static下面，所以正常情况url是static/filename ，但是可以通过static_url_path来改变这个url
    #static_folder主要是用来改变url的目录的，默认是static，可以通过这个变量来改变静态文件目录。
    #template_folder 用来改变templates的目录

    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_web_blueprint(app)



    db.init_app(app)

    with app.app_context():
        db.create_all()  ## 让sqlalchemy 所有的数据模型映射到数据库离去

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    mail.init_app(app)

    return app

