from flask import Flask

from extensions.routes_extension import register_routes
from extensions.injector_extension import register_dependency_injection
from extensions.exception_extension import register_exception_handler


def create_app():
    app = Flask(__name__)

    # will move to register_config soon
    app.config['ERROR_404_HELP'] = False

    register_routes(app)
    register_exception_handler(app)
    register_dependency_injection(app)
    return app
