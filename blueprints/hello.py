from flask import Blueprint

bp = Blueprint('hello', __name__, url_prefix='/')

@bp.route('/')
def hello():
    return 'Hello, world!'
