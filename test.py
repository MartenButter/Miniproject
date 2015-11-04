import sqla_createtaskdatabase

obj = sqla_createtaskdatabase.Task.getTask(1)
print (sqla_createtaskdatabase.Task.taskToList(obj))