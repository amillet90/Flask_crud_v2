from app import db
from Entity import Author


def main():
    db.drop_all()


if __name__ == '__main__':
    main()
