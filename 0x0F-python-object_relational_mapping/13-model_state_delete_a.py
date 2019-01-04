#!/usr/bin/python3
"""
deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sys import argv

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                argv[1], argv[2], argv[3]))

    session = sessionmaker(bind=engine)()
    results = session.query(State).all()
    for result in results:
        if 'a' in str(result):
            session.delete(result)
    session.commit()
    session.close()
