#!/usr/bin/python3
""" prints all City objects from the database hbtn_0e_14_usa """


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sys import argv

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                argv[1], argv[2], argv[3]))

    session = sessionmaker(bind=engine)()
    results = session.query(City, State).filter(
            State.id == City.state_id).order_by(City.id).all()
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
