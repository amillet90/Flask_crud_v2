import pymysql


# MySQL database configuration
# ----------------------------

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'password'
MYSQL_DATABASE = 'database'
MYSQL_CHARSET = 'utf8mb4'


# PyMySQL configuration
# ---------------------

# Read more at https://pymysql.readthedocs.io/en/latest/modules/cursors.html
PYMYSQL_CURSOR_CLASS = pymysql.cursors.DictCursor

# Logging configuration
# ---------------------

LOGGER_CONFIGURATION = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
}
