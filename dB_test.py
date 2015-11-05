from sqla_createtaskdatabase import *

# tasks = []

# for taskName in session.query(Task):
#     print(taskName.name)

# idParentTasks = Task.getAllParentTasksId()

def getParentTaskNames():
    names = []
    for taskName in session.query(Task.name).\
                    filter(Task.task_id==None):
        names.append(taskName[0])
    return names

tasks = getParentTaskNames()
print(tasks)

