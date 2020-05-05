from flask import *


c = Blueprint('main', __name__, url_prefix='/')


@c.route('/')
def index():
    return render_template('index.html.jj2')
