import sqla_createtaskdatabase
from data_validation import calculateProgressDownTree



taak = sqla_createtaskdatabase.Task.getTask(1)


print(calculateProgressDownTree(taak.id,taak.status, taak.duration))
