from app import db
from model import author


def main():
    db.drop_all()


if __name__ == '__main__':
    main()
