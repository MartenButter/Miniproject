import sqla_createtaskdatabase
import datetime
import math


def calculateProgress(id_,status,duration):

    l = sqla_createtaskdatabase.Task.getAllChildrenTasksId(id_)

    if (len(l) ==0):
        if(status == "finished"):
            return 1.0, duration
        else:
            return 0.0, duration
    else:

        sub_duration = 0
        for id_ in l:

            task = sqla_createtaskdatabase.Task.getTask(id_)
            tup = calculateProgress(id_,task.status,task.duration)


            if(tup[0] == 1.0):
                sub_duration += tup[1]


        return sub_duration/duration,duration




