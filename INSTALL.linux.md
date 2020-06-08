# Installation

## Installation de Python

Ce projet requiert au moins Python 3.6

### Installation avec gestionnaire des pacquets

#### Ubuntu/Debian

```shell
# apt-get install python3 python3-pip
```

#### Fedora/RHEL/CentOS

```shell
# dnf install python3 python3-pip
```

#### openSUSE

```shell
# zypper install python3 python3-pip
```

### Installation avec le programme d'installation

Si Python 3 n'existe pas sur votre distro, vous pouvez utiliser pyenv.

Voir cette page pour installer pyenv: https://github.com/pyenv/pyenv-installer

Après pyenv est installé, taper la commande suivante :

```shell
$ pyenv install 3.8.2
```

S'il y a une problème lors de compilation du Python, voir cette documentation :
https://github.com/pyenv/pyenv/wiki/Common-build-problems


## Installation des dépendances (Flask, SQLAlchemy, etc)

### Avec pip et requirements.txt

Dans le dossier racine du projet, taper la commande suivante :

```shell
$ pip install --user -r requirements.txt
```

### Avec Pipenv et Pipfile

[Pipenv][pipenv] est nécessaire pour installer les dépendances avec cette
méthode

```shell
$ pipenv install
$ pipenv shell # pour aller dans l'environnement virtuel pour ce projet
```

[pipenv]: https://github.com/pypa/pipenv
