class Config:
    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost/benchmark'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # APScheduler
    SCHEDULER_API_ENABLED = True
