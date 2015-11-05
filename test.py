import sqla_createtaskdatabase
from datavalidation import calculateProgressDownTree



taak = sqla_createtaskdatabase.Task.getTask(1)
duration = sqla_createtaskdatabase.Task.getDuration(taak)

print(duration)
