from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Date
from sqlalchemy import create_engine

Base = declarative_base()

class Task(Base):
    __tablename__ = 'Tasks'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    description = Column(String)
    task_id =  Column(Integer, ForeignKey('Tasks.id'))
    duration = Column(Integer)
    status = Column(String)
    responsible_person_id = Column(Integer, ForeignKey('Persons.id'))
    executer_person_id = Column(Integer, ForeignKey('Persons.id'))
    deadline = Column(DateTime)

class Person(Base):
    __tablename__ = 'Persons'

    id = Column(Integer,primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(Integer)
    function = Column(String)
    date_of_birth = Column(String)


if __name__ == '__main__':
    engine = create_engine('sqlite:///foo.db')
    Base.metadata.create_all(engine)