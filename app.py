import os
from logging.config import dictConfig
from importlib import import_module

import click
from flask import Flask, Blueprint
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

import config


db = SQLAlchemy()


def load_logging_config(app):
    dictConfig(app.config['LOGGER_CONFIGURATION'])


def make_instance_path(app):
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


def load_all_controllers(app):
    from Controller import AuteurController, IndexController

    controllers = [AuteurController.c, IndexController.c]
    for c in controllers:
        app.register_blueprint(c)


@click.command('create-all',
               short_help='Initialize database with tables')
@with_appcontext
def create_all_tables():
    db.create_all()


@click.command('drop-all',
               short_help='Drop all tables in database')
@with_appcontext
def drop_all_tables():
    db.drop_all()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config)
    load_logging_config(app)
    make_instance_path(app)
    db.init_app(app)

    from Entity.Auteur import Auteur
    app.cli.add_command(create_all_tables)
    app.cli.add_command(drop_all_tables)

    load_all_controllers(app)

    return app


if __name__ == '__main__':
    print("Run this application with 'flask run'.")
