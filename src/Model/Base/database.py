from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_connection():
    return create_engine("mysql+mysqlconnector://edu:flashcards@localhost/flashcards", echo=True)


def get_session():
    Session = sessionmaker(bind=get_connection())
    return Session()


def commit_insert(command):
    with get_connection().connect() as conn:
        result = conn.execute(command)
        conn.commit()

def commit_delete(commando):
    with get_session() as session:
        user = session.query(Topics).filter(Topics.id_assunto == 15).one()
        session.delete(user)
        session.commit()
