#!/usr/bin/python3
"""
Script 14-model_city_fetch_by_state.py that prints all City objects
from the database hbtn_0e_14_usa
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    usa = session.query(City, State) \
        .join(State, State.id == City.state_id) \
        .order_by(City.id.asc()) \
        .all()

    for city in usa:
        print("{}: ({}) {}".format(city.State.name,
                                   city.City.id,
                                   city.City.name))
