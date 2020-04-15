from flask import *


c = Blueprint('index', __name__, url_prefix='/')


@c.route('/')
def index():
    return render_template('index.html.jj2')
