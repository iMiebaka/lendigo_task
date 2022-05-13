from datetime import timedelta
import os
basedir = os.path.abspath(os.path.dirname(__file__))

def get_config(key, default):
    """Get the config from environment."""
    os.getenv(key=key, default=default)


class Config(object):
    ADMIN = os.environ.get('WA_ADMIN')
    ALLOWED_EXTENSIONS = set(['jpg', 'png'])
    APP_NAME = 'HackerNewsLendigo'
    COMMISSION_FEE = 0
    CONTRIBUTION_COMMISSION_SIGNUP_FEE = 50
    CONTRIBUTION_INTEREST = .08 
    DEBUG = False
    CELERY_BROKER_URL = 'redis://localhost:6379'
    JWT_SECRET_KEY = "secret-%-st)ff"
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'na-only-you-waka-come'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    MAIL_SENDER = 'HackerNewsLendigo <admin@hackernewstask.net>'
    MAIL_SUBJECT_PREFIX = '[hackernewstask]'
    SLOW_DB_QUERY_TIME = 0.5
    SSL_DISABLE = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = {'CACHE_TYPE': 'simple'}
    CELERY_BEAT_SCHEDULE = {
        'get-post': {
            'task': 'core.task.get_post',
            'schedule': timedelta(minutes=5), #Set this to to 3600 in development
            'args': ()
        },
    }

    TRANSACTIONS_PER_PAGE = 5
    UPLOAD_FOLDER = os.path.join(basedir, 'user_uploads')
    URL_PREFIX = ''
    # SQLALCHEMY_DATABASE_URI         = os.environ.get('DEV_DATABASE_URL') or \

    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    DEBUG = True
    SECRET_KEY = 'development'
    MAIL_SERVER = get_config("MAIL_SERVER", "")
    MAIL_PORT = get_config("MAIL_PORT", "")
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = get_config("MAIL_USERNAME", "")
    MAIL_SUPPRESS_SEND = False
    MAIL_PASSWORD = get_config("MAIL_PASSWORD", "")
    SQLALCHEMY_TRACK_NOTIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'db.sqlite3')


class Production(Config):
    '''
    TODO: If you want to switch to production, do not forget to create the mysql data
    username: root
    password: MYSQL_ROOT_PASSWORD  # Change be change
    database_name: hackernewstask
    '''
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:MYSQL_ROOT_PASSWORD@localhost:9906/hackernewstask"
    CELERY_BROKER_URL = 'redis://localhost:6379'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # email errors to the administrators
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls._MAIL_SENDER,
            toaddrs=[cls.WA_ADMIN],
            subject=cls.WA_MAIL_SUBJECT_PREFIX + ' Application Error',
            credentials=credentials,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


config = {
    'development': Development,
    'production': Production,
    'default': Development
}