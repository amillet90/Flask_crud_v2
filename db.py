import pymysql

from flask import current_app, g


def get():
    if 'db' not in g:
        g.db = pymysql.connect(
            host=current_app.config['MYSQL_HOST'],
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD'],
            db=current_app.config['MYSQL_DATABASE'],
            charset=current_app.config['MYSQL_CHARSET'],
            cursorclass=current_app.config['PYMYSQL_CURSOR_CLASS']
        )
    return g.db


def close():
    db = g.pop('db', None)

    if db is not None:
        db.close()
