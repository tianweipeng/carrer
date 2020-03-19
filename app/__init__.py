# -*- coding: utf-8 -*-

from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 创建函数工厂
def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    # 添加用户路由
    from .schools import school_spider as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/school_spider')
    return app
