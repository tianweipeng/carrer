import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # os.environ.get 从环境变量中读取配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    # UPLOADED_PHOTOS_DEST = os.environ.get('UPLOADED_PHOTO_DEST', os.getcwd() + '\\static\\photo\\')
    # UPLOADED_WORD_DEST = os.environ.get('UPLOADED_WORD_DEST', os.getcwd() + '\\static\\word\\')
    # MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.qq.com')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    # MAIL_USE_TLS = True
    # MAIL_DEFAULT_SENDER = "767339439@qq.com"
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '767339439@qq.com')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'cvwospcqqedtbcae')
    # FLASKY_MAIL_SUBJECT_PREFIX = "就业网信息"
    # FLASKY_MAIL_SENDER = 'Flasky Admin <767339439@qq.com>'
    # FLASKY_ADMIN = '767339439@qq.com'
    DEV_DATABASE_URL = 'mysql+pymysql://bee:Rhty@007@192.168.3.211:3306/carrer?charset=utf8mb4'
    TEST_DATABASE_URL = 'mysql+pymysql://bee:Rhty@007@192.168.3.211:3306/carrer?charset=utf8mb4'
    DATABASE_URL = 'mysql+pymysql://bee:Rhty@007@192.168.3.211:3306/carrer?charset=utf8mb4'
    # 分页每页条数
    # FLASKY_POSTS_PER_PAGE = 10
    # 配置连接池大小为30
    SQLALCHEMY_POOL_SIZE = 30
    # 超出连接池大小后可添加10个链接
    SQLALCHEMY_MAX_OVERFLOW = 10
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 1 * 1024 * 1024

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = Config.DEV_DATABASE_URL


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
