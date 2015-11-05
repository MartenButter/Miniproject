import sqla_createtaskdatabase
import datetime
import math


def calculateProgress(id_,status,duration):

    l = sqla_createtaskdatabase.Task.getAllChildrenTasksId(id_)

    if (len(l) == 0):
        task = sqla_createtaskdatabase.Task.getTask(id_)
        if(status == "finished"):
            if(task.progress != 1.0):

                task.progress = 1.0
                sqla_createtaskdatabase.Task.updateTask(task)

                return 1.0, duration
            else:
                return 1.0, duration
        else:
            return 0.0, duration
    else:
        if(status == 'finished'):
            return 1.0, duration
        else:
            sub_duration = 0
            for child_id in l:
                print(id_)
                task = sqla_createtaskdatabase.Task.getTask(child_id)

                tup = calculateProgress(child_id,task.status,task.duration)

                if(tup[0] == 1.0):
                    sub_duration += tup[1]
                else:
                    sub_duration += tup[1]*tup[0]

            progress = round(sub_duration/duration,2)
            print(progress,id_)
            task.progress = progress
            sqla_createtaskdatabase.Task.updateTask(task)

            return progress,duration




