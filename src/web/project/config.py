import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = f"{os.environ.get('APP_FOLDER')}/project/static"
    MEDIA_FOLDER = f"{os.environ.get('APP_FOLDER')}/project/media"
