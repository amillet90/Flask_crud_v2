import re

from flask import *

from app import db
from Entity.Auteur import Auteur

c = Blueprint('auteur', __name__, url_prefix='/auteur')


@c.route('/show')
def show():
    return render_template('auteur/showAuteurs.html.jj2', auteurs=Auteur.query.all())


@c.route('/supprimer/<int:id>', methods=['GET'])
def supprimer(id):
    auteur = Auteur.query.filter_by(id=id).first_or_404()

    if auteur.oeuvres:
        return render_template('auteur/ErrorDeleteAuteur.html.jj2', nombre=len(auteur.oeuvres)), 400

    db.session.delete(auteur)
    db.session.commit()

    return redirect(url_for('auteur.show'))


@c.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'GET':
        return render_template('auteur/addAuteur.html.jj2', errors=dict())

    valid, errors = valider_form()

    if valid:
        auteur = Auteur(prenom=request.form['prenom'],
                        nom=request.form['nom'])
        db.session.add(auteur)
        db.session.commit()

        return redirect(url_for('auteur.show'))
    else:
        return render_template('auteur/addAuteur.html.jj2', errors=errors)


@c.route('/modifier/<int:id>', methods=['GET', 'POST'])
def modifier(id):
    auteur = Auteur.query.filter_by(id=id).first_or_404()

    if request.method == 'GET':
        return render_template('auteur/editAuteur.html.jj2', auteur=auteur,
                               errors=dict())

    valid, errors = valider_form()

    if valid:
        auteur.prenom = request.form['prenom']
        auteur.nom = request.form['nom']
        db.session.commit()

        return redirect(url_for('auteur.show'))
    else:
        return render_template('auteur/editAuteur.html.jj2', auteur=auteur,
                               errors=errors)


def valider_form():
    valid = True
    errors = dict()

    if not re.match(r'\w{2,}', request.form['prenom']):
        # flash('Prenom doit avoir au moins deux caractères')
        errors['prenom'] = 'Prenom doit avoir au moins deux caractères'
        valid = False

    if not re.match(r'\w{2,}', request.form['nom']):
        # flash('Nom doit avoir au moins deux caractères')
        errors['nom'] = 'Nom doit avoir au moins deux caractères'
        valid = False

    return (valid, errors)
