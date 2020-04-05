from flask import *

from app import db
from Entity.Author import Author

c = Blueprint('author', __name__, url_prefix='/author')


@c.route('/')
def index():
    return render_template('author/index.html', authors=Author.query.all())


@c.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    author =  Author.query.filter_by(id=id).first_or_404()

    db.session.delete(author)
    db.session.commit()

    return redirect(url_for('author.index'))


@c.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('author/add.html')

    author = Author(first_name=request.form['first_name'],
                    last_name=request.form['last_name'])

    db.session.add(author)
    db.session.commit()

    return redirect(url_for('author.index'))


@c.route('/modify/<int:id>', methods=['GET', 'POST'])
def modify(id):
    author =  Author.query.filter_by(id=id).first_or_404()

    if request.method == 'GET':
        return render_template('author/modify.html', author=author)

    author.first_name = request.form['first_name']
    author.last_name = request.form['last_name']
    db.session.commit()

    return redirect(url_for('author.index'))
