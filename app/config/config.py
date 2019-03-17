"""
    Configuration
    _______________
    This is module for storing all configuration for various environments
"""
import os

class Config:
    """ This is base class for configuration """
    DEBUG = False

    #mongodb://[username:password@]host1[:port1][,...hostN[:portN]]][/[database][?options]]
    DATABASE = {
        "DRIVER"   : os.getenv('DB_DRIVER') or "mongodb", # sqlite // postgresql // mysql
        "USERNAME" : os.getenv('DB_USERNAME') or "flask_starter",
        "PASSWORD" : os.getenv('DB_PASSWORD') or "somepassword",
        "HOST_NAME": os.getenv('DB_HOSTNAME') or "localhost",
        "PORT"     : os.getenv('DB_PORT') or "27017",
        "NAME"     : os.getenv('DB_NAME') or 'db_flask_starter'
    }

    SENTRY_CONFIG = {}

    # FLASK RESTPLUS
    ERROR_INCLUDE_MESSAGE = False
#end class


class DevelopmentConfig(Config):
    """ This is class for development configuration """
    DEBUG = True

    DATABASE = Config.DATABASE
    MONGO_URI = "{}://{}:{}@{}:{}/{}".format(DATABASE["DRIVER"],
                                          DATABASE["USERNAME"],
                                          DATABASE["PASSWORD"],
                                          DATABASE["HOST_NAME"],
                                          DATABASE["PORT"],
                                          DATABASE["NAME"])
#end class


class TestingConfig(Config):
    """ This is class for testing configuration """
    DEBUG = True
    TESTING = True

    DATABASE = Config.DATABASE
    MONGO_URI = "{}://{}:{}@{}:{}/{}".format(DATABASE["DRIVER"],
                                          DATABASE["USERNAME"],
                                          DATABASE["PASSWORD"],
                                          DATABASE["HOST_NAME"],
                                          DATABASE["PORT"],
                                          DATABASE["NAME"])


    SENTRY_CONFIG = {}
#end class


class ProductionConfig(Config):
    """ This is class for production configuration """
    DEBUG = False

    DATABASE = Config.DATABASE
    MONGO_URI = "{}://{}:{}@{}:{}/{}".format(DATABASE["DRIVER"],
                                          DATABASE["USERNAME"],
                                          DATABASE["PASSWORD"],
                                          DATABASE["HOST_NAME"],
                                          DATABASE["PORT"],
                                          DATABASE["NAME"])
    
    PRESERVE_CONTEXT_ON_EXCEPTION = False

    SENTRY_CONFIG = Config.SENTRY_CONFIG
    SENTRY_CONFIG["dsn"] = os.environ.get("SENTRY_DSN")
#end class

CONFIG_BY_NAME = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
