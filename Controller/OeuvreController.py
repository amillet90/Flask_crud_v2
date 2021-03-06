import datetime
import os
import re

from flask import *

from app import db
from Entity.Auteur import Auteur
from Entity.Oeuvre import Oeuvre

bp = Blueprint('oeuvre', __name__, url_prefix='/oeuvre')


@bp.route('/show')
def show():
    return render_template('oeuvre/showOeuvre.html.jj2', oeuvres=Oeuvre.query.all())


@bp.route('/supprimer/<int:id>', methods=['GET'])
def supprimer(id):
    oeuvre = Oeuvre.query.filter_by(id=id).first_or_404()

    db.session.delete(oeuvre)
    db.session.commit()

    return redirect(url_for('oeuvre.show'))


@bp.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'GET':
        return render_template('oeuvre/addOeuvre.html.jj2',
                               auteurs=Auteur.query.all(), errors=dict())

    valid, errors = valider_form()

    if valid:
        auteur = Auteur.query.filter_by(id=request.form['auteur_id']).first()

        oeuvre = Oeuvre(titre=request.form['titre'],
                        dateParution=request.form['dateParution'],
                        photo=request.form['photo'],
                        prix=request.form['prix'],
                        auteur=auteur)
        db.session.add(oeuvre)
        db.session.commit()

        return redirect(url_for('oeuvre.show'))
    else:
        return render_template('oeuvre/addOeuvre.html.jj2',
                               auteurs=Auteur.query.all(), errors=errors)


@bp.route('/modifier/<int:id>', methods=['GET', 'POST'])
def modifier(id):
    oeuvre = Oeuvre.query.filter_by(id=id).first_or_404()

    if request.method == 'GET':
        return render_template('oeuvre/editOeuvre.html.jj2',
                               oeuvre=oeuvre, auteurs=Auteur.query.all(),
                               errors=dict())

    valid, errors = valider_form()

    if valid:
        auteur = Auteur.query.filter_by(id=request.form['auteur_id']).first()

        photo = request.form['photo']

        if not photo:
            photo = 'no_photo.jpeg'

        oeuvre.titre = request.form['titre']
        oeuvre.dateParution = request.form['dateParution']
        oeuvre.photo = photo
        oeuvre.auteur = auteur
        oeuvre.prix = request.form['prix']

        db.session.commit()

        return redirect(url_for('oeuvre.show'))
    else:
        return render_template('oeuvre/editOeuvre.html.jj2',
                               oeuvre=oeuvre, auteurs=Auteur.query.all(),
                               errors=errors)


def valider_form():
    valid = True
    errors = dict()

    auteur = Auteur.query.filter_by(id=request.form['auteur_id']).first()

    if auteur is None:
        # flash("Auteur n'existe pas")
        errors['auteur'] = "Auteur n'existe pas"
        valid = False

    if not re.match(r'\w{2,}', request.form['titre']):
        # flash('Titre doit avoir au moins deux caractères')
        errors['titre'] = "Titre doit avoir au moins deux caractères"
        valid = False

    try:
        datetime.datetime.strptime(request.form['dateParution'], '%Y-%m-%d')
    except ValueError:
        # flash("Date n'est pas valide")
        errors['dateParution'] = "Date n'est pas valide"
        valid = False

    if request.form['photo']:
        photo_path = os.path.join(current_app.root_path,
                                  'static', 'assets', 'images', request.form['photo'])

        if not os.path.isfile(photo_path):
            # flash(f"Photo n'existe pas: { photo_path }")
            errors['photo'] = f"Photo n'existe pas: { photo_path }"
            valid = False

    try:
        float(request.form['prix'])
    except ValueError:
        # flash("Prix n'est pas valide")
        errors['prix'] = "Prix n'est pas valide"
        valid = False

    return (valid, errors)
