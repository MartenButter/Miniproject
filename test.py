import sqla_createtaskdatabase
from datavalidation import calculateProgressDownTree


childrenDCT = sqla_createtaskdatabase.Task.getAllChildrenTasksAndId(1)
for child in childrenDCT:
    print(childrenDCT[child].name)
