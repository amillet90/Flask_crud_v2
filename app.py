import os
from logging.config import dictConfig
from importlib import import_module

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

import config


app = Flask(__name__, instance_relative_config=True)
app.config.from_object(config)

db = SQLAlchemy(app)


def load_logging_config():
    dictConfig(app.config['LOGGER_CONFIGURATION'])


def make_instance_path():
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


def load_all_controllers():
    from Controller import AuthorController, MainController

    controllers = [AuthorController.c, MainController.c]
    for c in controllers:
        app.register_blueprint(c)


if __name__ == '__main__':
    load_logging_config()
    make_instance_path()
    load_all_controllers()

    app.run(debug=True)
