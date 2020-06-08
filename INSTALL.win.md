# Installation

## Installation de Python

Ce projet requiert au moins Python 3.6

### Installation avec gestionnaire des pacquets

[Chocolatey][chocolatey] est nécessaire pour installer Python avec cette méthode

```shell
PS C:\> choco install python
```

### Installation avec le programme d'installation

Aller sur https://python.org et télécharger le programme d'installation de Python.

## Installation des dépendances (Flask, SQLAlchemy, etc)

Dans le dossier racine du projet, taper la commande suivante :

```shell
PS C:\> python -m pip install --user -r requirements.txt
```

[chocolatey]: https://chocolatey.org
