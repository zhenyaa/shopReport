from os import path


class Config(object):

    DEBUG = False
    REMEMBER_COOKIE_DURATION = 200

class Development(Config):
    SECRET_KEY = 'MySecretKey'
    SESSION_TYPE = 'filesystem'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:12358134@localhost/report'
    USE_RELOADER = True
    USE_DEBUGGER = True

class Production(Config):
    pass