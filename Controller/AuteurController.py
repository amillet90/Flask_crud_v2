from flask import *

from app import db
from Entity.Auteur import Auteur

c = Blueprint('auteur', __name__, url_prefix='/auteur')


@c.route('/')
def index():
    return render_template('auteur/index.html', auteurs=Auteur.query.all())


@c.route('/supprimer/<int:id>', methods=['GET'])
def supprimer(id):
    auteur = Auteur.query.filter_by(id=id).first_or_404()

    db.session.delete(auteur)
    db.session.commit()

    return redirect(url_for('auteur.index'))


@c.route('/ajouter', methods=['GET', 'POST'])
def ajouter():
    if request.method == 'GET':
        return render_template('auteur/ajouter.html')

    auteur = Auteur(prenom=request.form['prenom'],
                    nom=request.form['nom'])

    db.session.add(auteur)
    db.session.commit()

    return redirect(url_for('auteur.index'))


@c.route('/modifier/<int:id>', methods=['GET', 'POST'])
def modifier(id):
    auteur = Auteur.query.filter_by(id=id).first_or_404()

    if request.method == 'GET':
        return render_template('auteur/modifier.html', auteur=auteur)

    auteur.prenom = request.form['prenom']
    auteur.nom = request.form['nom']
    db.session.commit()

    return redirect(url_for('auteur.index'))
