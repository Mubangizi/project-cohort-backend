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
    SQLALCHEMY_DATABASE_URI = os.getenv("postgres://piphnntiovpksk:1181ae1a6858f6e1e1daf8ebd570fca784e2daf79d36d98f06cdadf8db1c020e@ec2-34-198-243-120.compute-1.amazonaws.com:5432/dd386774tg2nab")


app_config = {"development": Development, "testing": Testing, "production": Production}
