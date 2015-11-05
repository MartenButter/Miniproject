from sqla_createtaskdatabase import *

tasks = []

for taskName in session.query(Task):
    print(taskName.name)

