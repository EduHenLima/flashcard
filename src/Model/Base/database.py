from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_connection():
    return create_engine("mysql+mysqlconnector://edu:flashcards@localhost/flashcards", echo=True)


def get_session():
    Session = sessionmaker(bind=get_connection())
    return Session()
