import os


class Base:
    """ base config """


class Development(Base):
    """ development config """

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql:///cohort_db"

class Testing(Base):
    """ test environment config """

    TESTING = True
    DEBUG = True
    # use a separate db

    SQLALCHEMY_DATABASE_URI = "postgresql:///cohort_test_db"


class Production(Base):
    """ production config """

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgres://saweforfocreht:7427272b8205d41b089c7f201158e6de682dc598cf422c8736502440f198455e@ec2-54-159-112-44.compute-1.amazonaws.com:5432/d127gne4u5bef3"


app_config = {"development": Development, "testing": Testing, "production": Production}
