import sqlite3
import names
import random
from myfunctions import open_conn_ret_cur, count_table

# Fills the persons table with 100 random names.
def fill_persons(cur):

    # 100 random persons...
    for i in range(0,100):
        # Creates Person with random first and last name. Also other random functions are inserted.
        person = ( names.get_first_name(), names.get_last_name(),' ',random.randint(60000 , 999999), "functie", 0)
        # Inserts record in the table.
        cur.execute('''INSERT INTO Persons
                    VALUES(NULL,?,?,?,?,?,?);''', person)
# Fills the groups table with 10 groups.
def fill_groups(cur):
    # Looks at how long the persons table is so that there are no out of bound values.
    length_persons = count_table(cur,'Persons')

    # 10 groups
    for i in range(0,10):

        # Creates the groups. Random values for size and a random group leader.
        group = (random.randint(1,6),random.randint(1,length_persons + 1))

        # Inserts record in the table.
        cur.execute('''INSERT INTO Groups
                       VALUES(NULL,?,?);''', group)

# Fills the groups_persons table with persons and groups.
def fill_groups_persons(cur,conn):
    # Creates extra cursor, because we don't want have any conflicts....
    groupcursor = conn.cursor()

    # Gets all the groups
    groupcursor.execute('''SELECT * FROM Groups''')
    # Loop for every row in groups.
    while True:
        # Row is....
        row = groupcursor.fetchone()
        # If now rows left, break
        if row == None:
            break
        # Insert the group leader first.
        cur.execute('''INSERT INTO Groups_Persons VALUES(?,?)''',(row[0],row[2]))

        # For the size adds a person minus one (Groupleader)
        for i in range(1,row[1]):

            # Construction to prevent a group leader to be added twice.
            while True:
                person = list(cur.execute('''SELECT * FROM Persons ORDER BY RANDOM() LIMIT 1;'''))
                # Is the person the group leader?
                if person[0][0] != row[2]:
                    break
            # Add person to group in table!
            cur.execute('''INSERT INTO Groups_Persons VALUES(?,?)''',(row[0],person[0][0]))

# Lets put it all together!
def fill_database():
    conn = sqlite3.connect('task_database.db')
    cur = conn.cursor()
    fill_persons(cur)
    fill_groups(cur)
    fill_groups_persons(cur,conn)

    conn.commit()
    conn.close()