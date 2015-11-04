from names import get_first_name, get_last_name
from sqla_createtaskdatabase import Person
import random
from datetime import date
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///foo.db')
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

def fill_persons():

    # 100 random persons...
    for i in range(0,100):
        # Creates Person with random first and last name. Also other random functions are inserted.
        person = ( get_first_name(), get_last_name(),' ',random.randint(60000 , 999999), "functie", 0)
        # Inserts record in the table.
    for i in range(100):


        persoon = Person(first_name=get_first_name(),last_name=get_last_name(),email="",phone_number=681365020,function="function",date_of_birth = "12/12/12")

        session.add(persoon)

    session.commit()