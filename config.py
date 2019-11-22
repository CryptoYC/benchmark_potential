class Config:
    """
    Set Flask configuration vars from .env file.
    """
    # General
    TESTING = True
    FLASK_DEBUG = True
    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost/benchmark'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # APScheduler
    JOBS = [
        {
            'id': 'job',
            'func': '__main__:get_repositories_topic_task',
            'args': None,
            'trigger': 'interval',
            'minutes': 1,
        }
    ]
