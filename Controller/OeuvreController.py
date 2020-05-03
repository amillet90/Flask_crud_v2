import re

from flask import *

from app import db
from Entity.Auteur import Auteur
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


@bp.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'GET':
        return render_template('oeuvre/ajouter.html.jj2', auteurs=Auteur.query.all())

    if valider_form():
        auteur = Auteur.query.filter_by(id=request.form['auteur_id']).first()

        oeuvre = Oeuvre(titre=request.form['titre'],
                        dateParution=request.form['dateParution'],
                        photo=request.form['photo'],
                        auteur=auteur)
        db.session.add(oeuvre)
        db.session.commit()

        return redirect(url_for('oeuvre.index'))
    else:
        return redirect(url_for('oeuvre.ajouter'))


def valider_form():
    valid = True

    return valid
