import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
NAME_DB = os.getenv('NAME_DB')
USER_DB = os.getenv('USER_DB')
PASSWORD_DB = os.getenv('PASSWORD_DB')

class Development(object):
  DEBUG = True
  TESTING = False
  SQLALCHEMY_DATABASE_URI = f"postgresql://{USER_DB}:{PASSWORD_DB}@localhost:5432/{NAME_DB}-development"
  SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

class Production(object):
  DEBUG = False
  TESTING = False
  SQLALCHEMY_DATABASE_URI = f"postgresql://{USER_DB}:{PASSWORD_DB}@localhost:5432/{NAME_DB}-production"
  SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

app_config = {
  "development": Development, 
  "production": Production
}