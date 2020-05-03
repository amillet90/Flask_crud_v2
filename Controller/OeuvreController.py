import datetime
import os
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


@bp.route('/modifier/<int:id>', methods=['GET', 'POST'])
def modifier(id):
    oeuvre = Oeuvre.query.filter_by(id=id).first_or_404()

    if request.method == 'GET':
        return render_template('oeuvre/modifier.html.jj2',
                               oeuvre=oeuvre, auteurs=Auteur.query.all())

    if valider_form():
        auteur = Auteur.query.filter_by(id=request.form['auteur_id']).first()

        oeuvre.titre = request.form['titre'],
        oeuvre.dateParution = request.form['dateParution']
        oeuvre.photo = request.form['photo']
        oeuvre.auteur = auteur
        db.session.commit()

        return redirect(url_for('oeuvre.index'))
    else:
        return redirect(url_for('oeuvre.modifier', id=id))


def valider_form():
    valid = True

    auteur = Auteur.query.filter_by(id=request.form['auteur_id']).first()

    if auteur is None:
        flash("Auteur n'existe pas.")
        valid = False

    if not re.match(r'\w{2,}', request.form['titre']):
        flash('Titre doit avoir au moins deux caratères')
        valid = False

    try:
        datetime.datetime.strptime(request.form['dateParution'], '%Y-%m-%d')
    except ValueError:
        flash("Date n'est pas valide")
        valid = False

    photo_path = os.path.join(current_app.root_path, 'static', 'images', request.form['photo'])

    if not os.path.isfile(photo_path):
        flash(f"Photo n'existe pas {photo_path}")
        valid = False

    return valid
