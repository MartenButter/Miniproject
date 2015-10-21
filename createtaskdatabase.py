__author__ = 'Marten'

import sqlite3

# Lets put it all together
def create_database():
    # Create database/setup connection.
    conn = sqlite3.connect('task_database.db')

    # Create cursor object for statements.
    cur =  conn.cursor()

    # Create Persons Table
    cur.execute('''CREATE TABLE Persons(        id INTEGER PRIMARY KEY,
                                                firstname TEXT,
                                                lastname TEXT,
                                                email TEXT,
                                                phonenumber INTEGER,
                                                function TEXT,
                                                dateofbirth INTEGER); ''')

    # Create Groups Table
    cur.execute('''CREATE TABLE Groups (        id INTEGER PRIMARY KEY,
                                                size INTEGER,
                                                groupleader INTEGER,
                                                FOREIGN KEY(groupleader) REFERENCES Persons(id)); ''')
    # Create Groups_Persons Table
    cur.execute('''CREATE TABLE Groups_Persons (group_id INTEGER,
                                                person_id INTEGER,
                                                FOREIGN KEY(group_id) REFERENCES Groups(id),
                                                FOREIGN KEY(person_id) REFERENCES Persons(id));''')

    # Create Task Table
    cur.execute('''CREATE TABLE Tasks (         id INTEGER PRIMARY KEY,
                                                name TEXT,
                                                done TEXT,
                                                description TEXT,
                                                parent_task_id INTEGER,
                                                duration TEXT,
                                                status TEXT,
                                                responsible_person_id INTEGER,
                                                executer_group_id INTEGER,
                                                deadline TEXT,

                                                FOREIGN KEY(parent_task_id) REFERENCES Tasks(id),
                                                FOREIGN KEY(executer_group_id) REFERENCES Groups(id),
                                                FOREIGN KEY(responsible_person_id) REFERENCES Persons(id));''')
    # Create Functions Table
    cur.execute('''CREATE TABLE Functions (     id INTEGER PRIMARY KEY,
                                                name TEXT,
                                                description TEXT)''')

    # Create Needs Table
    cur.execute('''CREATE TABLE Needs (         id INTEGER,
                                                name TEXT,
                                                description TEXT)''')


    # Create Tasks_Needs Table
    cur.execute('''CREATE TABLE Tasks_Needs (   Task_id INTEGER,
                                                Need_id INTEGER,
                                                done TEXT,
                                                FOREIGN KEY(Task_id) REFERENCES Tasks(id),
                                                FOREIGN KEY(Need_id) REFERENCES Needs(id));''')



    # Commit the changes to the database.
    conn.commit()



    # Close the database connection.
    conn.close()