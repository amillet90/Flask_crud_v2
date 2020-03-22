import os
from logging.config import dictConfig
from importlib import import_module

from flask import Flask, Blueprint


def load_config(app):
    config = import_module('config')

    app.config.from_object(config)


def load_logging_config(app):
    dictConfig(app.config['LOGGER_CONFIGURATION'])


def make_instance_path(app):
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


def load_all_controllers(app):
    parent_module = import_module('controller')

    modules = parent_module.__all__

    for mod_name in modules:
        mod = import_module(f'controller.{mod_name}')
        for name, attr in mod.__dict__.items():
            if isinstance(attr, Blueprint):
                app.register_blueprint(attr)
                app.logger.info(f'registered: controller.{mod_name}.{name}')


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    load_config(app)
    load_logging_config(app)
    make_instance_path(app)
    load_all_controllers(app)

    return app
