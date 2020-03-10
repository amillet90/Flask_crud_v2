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
