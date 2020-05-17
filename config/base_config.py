"""Flask config class."""
import os


class BaseConfig:
    """Base config vars."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')
