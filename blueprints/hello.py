from flask import Blueprint, render_template, request


bp = Blueprint('hello', __name__, url_prefix='/')


@bp.route('/')
def hello():
    name = request.args.get('name', 'world')
    return render_template('hello.html', name=name)
