#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa """


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sys import argv

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                argv[1], argv[2], argv[3]))

    session = sessionmaker(bind=engine)
    results = session().query(State).first()
    if results:
        print("{}: {}".format(results.id, results.name))
    else:
        print("Nothing")
    session().close()
