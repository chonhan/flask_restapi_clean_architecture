"""Flask config class."""
import os
from .base_config import BaseConfig


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('PROD_DATABASE_URI')
