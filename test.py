import sqla_createtaskdatabase
from datavalidation import calculateProgressDownTree



taak = sqla_createtaskdatabase.Task.getTask(1)


print(calculateProgressDownTree(taak.id,taak.status, taak.duration))
