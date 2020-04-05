from app import db
from Entity import Author


def main():
    db.create_all()


if __name__ == '__main__':
    main()
