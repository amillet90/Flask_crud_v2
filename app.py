import os

from flask import Flask


def register_routes_entry(app):
    import routes

    for entry in routes.routes:
        entry.register(app)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    register_routes_entry(app)

    return app
