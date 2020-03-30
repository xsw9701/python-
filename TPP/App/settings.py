import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALIPAY_APPID = "2016091800537304"

APP_PRIVATE_KEY = open(os.path.join(BASE_DIR, 'alipay_config/app_rsa_private_key.pem'), 'r').read()

ALIPAY_PUBLIC_KEY = open(os.path.join(BASE_DIR, 'alipay_config/alipay_rsa_public_key.pem'), 'r').read()

def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE") or "sqlite"
    driver = dbinfo.get("DRIVER") or "sqlite"
    user = dbinfo.get("USER") or ""
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST") or ""
    port = dbinfo.get("PORT") or ""
    name = dbinfo.get("NAME") or ""
    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "xusiwei"
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(31)
    #  默认是31天


class DevelopConfig(Config):
    DEBUG = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "mysqlconnector",
        "USER": "root",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "3307",
        "NAME": "flasktpp"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)
    #邮箱配置
    MAIL_SERVER = "smtp.126.com"
    MAIL_PORT = 25
    MAIL_USERNAME = "a2991495862@126.com"
    MAIL_PASSWORD = "abc123456789"
    MAIL_DEFAULT_SENDER = MAIL_USERNAME



class TestConfig(Config):
    TESTING = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "mysqlconnector",
        "USER": "root",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "3307",
        "NAME": "flaskdb"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagingConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "mysqlconnector",
        "USER": "root",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "3307",
        "NAME": "flaskdb"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "mysqlconnector",
        "USER": "root",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "3307",
        "NAME": "flaskdb"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)
    # 四套环境，开发环境，测试环境，演示环境，线上环境


envs = {
    "develop": DevelopConfig,
    "testing": TestConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}
ADMINS = ('憨憨管理员', 'GJY')

FILE_PATH_PREFIX = "/static/uploads/icons"

UPLOADS_DIR = os.path.join(BASE_DIR, 'App/static/uploads/icons')