import os
class BaseConfig:
  TESTING = False
  SQLALCHEMY_TRACK_NOTIFICATIONS = False

class DevelopmentConfig(BaseConfig):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_DEV_URL')

class TestingConfig(BaseConfig):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')

class ProductionConfig(BaseConfig):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')