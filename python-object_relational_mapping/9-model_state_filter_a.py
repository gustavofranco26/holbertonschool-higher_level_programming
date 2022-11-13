#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter "a"
from the database hbtn_0e_6_usa
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    a_states = session.query(State) \
        .order_by(State.id.asc()) \
        .filter(State.name.ilike('%a%')) \
        .all()

    for a_state in a_states:
        print("{}: {}".format(a_state.id, a_state.name))
