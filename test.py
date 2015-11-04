import sqla_createtaskdatabase
from data_validation import calculateProgress



taak = sqla_createtaskdatabase.Task.getTask(1)

print(calculateProgress(taak.id,taak.status, taak.duration))
