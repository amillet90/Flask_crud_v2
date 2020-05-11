# Flask MVC sample project

> **This project is not ideal for any production projects whatsoever.**


> This project is simply to illustrate how MVC works under the hood. In no way
> what-so-ever that this project implies a good MVC. This project is simply made
> as a tool of teaching, nothing more, nothing less.

## Lancer le serveur web du projet

```shell
$ flask run
```

Si `flask` n'existe pas, assurer que `~/.local/bin` est dans votre `$PATH`.

## Installation

### Installation de Python

Ce projet requiert au moins Python 3.6

#### Installation avec gestionnaire des pacquets

##### Ubuntu/Debian

```shell
# apt-get install python3 python3-pip
```

##### Fedora/RHEL/CentOS

```shell
# dnf install python3 python3-pip
```

##### openSUSE

```shell
# zypper install python3 python3-pip
```

##### macOS

[Homebrew][homebrew] est nécessaire pour installer Python avec cette méthode

```shell
$ brew install python
```

##### Windows (Chocolatey)

[Chocolatey][chocolatey] est nécessaire pour installer Python avec cette méthode

```shell
PS C:\> choco install python
```

#### Installation avec le programme d'installation

##### Windows

Aller sur https://python.org et télécharger le programme d'installation de Python.

#### Installation avec pyenv (Linux, macOS)

Si Python 3 n'existe pas sur votre distro, vous pouvez utiliser pyenv.

Voir cette page pour installer pyenv: https://github.com/pyenv/pyenv-installer

Après pyenv est installé, taper la commande suivante :

```shell
$ pyenv install 3.8.2
```

S'il y a une problème lors de compilation du Python, voir cette documentation :
https://github.com/pyenv/pyenv/wiki/Common-build-problems

### Installation des dépendances (Flask, SQLAlchemy, etc)

#### Avec pip et requirements.txt

Dans le dossier racine du projet, taper la commande suivante :

```shell
$ pip install --user -r requirements.txt
```

#### Avec Pipenv et Pipfile

[Pipenv][pipenv] est nécessaire pour installer les dépendances avec cette
méthode

```shell
$ pipenv install
$ pipenv shell # pour aller dans l'environnement virtuel pour ce projet
```


## Configuration

### Configuration du BDD

Ouvrir le fichier `config.py` et modifier les variables `MYSQL_HOSTNAME`,
`MYSQL_DATABASE`, `MYSQL_USERNAME` et `MYSQL_PASSWORD`.

Par exemple :

```python
MYSQL_HOSTNAME = 'balthasar.magi.nerv.gov.jp`
MYSQL_DATABASE = 'detabesu'
MYSQL_USERNAME = 'soryuu'
MYSQL_PASSWORD = 'passwort'
```

### Initialiser le BDD

Pour initialiser le BDD avec les éntités, taper cette commande :

```shell
$ flask create-all
```

[homebrew]: https://brew.sh
[chocolatey]: https://chocolatey.org
[pipenv]: https://github.com/pypa/pipenv
