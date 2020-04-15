import re

from flask import *

from app import db
from Entity.Oeuvre import Oeuvre

bp = Blueprint('oeuvre', __name__, url_prefix='/oeuvre')


@bp.route('/')
def index():
    return render_template('oeuvre/index.html.jj2', oeuvres=Oeuvre.query.all())


@bp.route('/supprimer/<int:id>', methods=['GET'])
def supprimer(id):
    oeuvre = Oeuvre.query.filter_by(id=id).first_or_404()

    db.session.delete(oeuvre)
    db.session.commit()

    return redirect(url_for('oeuvre.index'))
