from .prod_config import ProductionConfig
from .dev_config import DevelopmentConfig

configurations = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
