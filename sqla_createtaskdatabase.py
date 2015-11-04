from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///foo.db')
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


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
    deadline = Column(String)
    progress = Column(Float)

    #Gets all the Id's of all parent tasks
    def getAllParentTasksId():
        lst = []
        for instance in session.query(Task).\
                filter(Task.task_id==None):
            lst.append(instance.id)
        #Returns them in a list
        return lst

    #Gets all the Id's of all children tasks of specified parent Id
    def getAllChildrenTasksId(parent_id):
        lst = []
        for instance in session.query(Task).\
                filter(Task.task_id==parent_id):
            lst.append(instance.id)
        #Returns a list

        return lst


    #Gets an Task object with specified Id
    def getTask(id):
        for instance in session.query(Task).\
                filter(Task.id==id):
            #Returns the Task object
            return instance

    #Gets all Task objects
    def getAllParentTasksAndId():
        lst = Task.getAllParentTasksId()
        task_lst = []
        for i in lst:
            task_lst.Append(Task.getTask(i))
        #Returns a dictionary with Id's as key and Task objects as value
        return dict(zip(lst,task_lst))

    #Gets all children Task objects of specified Id
    def getAllChildrenTasksAndId(parent_id):
        lst = Task.getAllChildrenTasksId(parent_id)
        task_lst =[]
        for i in lst:
            task_lst.append(Task.getTask(i))
        #Returns a dictionary with Id's as key and Task objects as value
        return dict(zip(lst,task_lst))

    #Updates an Task object in the database
    def updateTask(self):
        session.add(self)
        session.commit()

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