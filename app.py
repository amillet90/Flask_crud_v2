import os
from logging.config import dictConfig
from importlib import import_module

import click
from flask import Flask, Blueprint
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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


def load_modules_from_parent(name):
    parent_module = import_module(name)

    return [import_module(f'{name}.{module_name}')
            for module_name in parent_module.__all__]


def load_all_controllers(app):
    for module in load_modules_from_parent('controller'):
        for attr in dir(module):
            attr = getattr(module, attr)
            if isinstance(attr, Blueprint):
                app.register_blueprint(attr)


@click.command('init-db',
               short_help='Initialize database and populate with models')
@with_appcontext
def create_all_models_command():
    load_modules_from_parent('model')
    db.create_all()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    load_config(app)
    load_logging_config(app)
    make_instance_path(app)
    db.init_app(app)
    app.cli.add_command(create_all_models_command)
    load_all_controllers(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
