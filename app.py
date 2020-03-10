import os

from flask import Flask


def load_config(app):
    import config

    app.config.from_object(config)


def make_instance_path(app):
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


def register_routes_entry(app):
    import routes

    for entry in routes.routes:
        entry.register(app)


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    load_config(app)
    make_instance_path(app)
    register_routes_entry(app)

    return app
