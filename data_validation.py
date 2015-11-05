import sqla_createtaskdatabase
import datetime
import math


def calculateProgressDownTree(id_,status,duration):
    print("calculating progress down tree of:",id_)
    l = sqla_createtaskdatabase.Task.getAllChildrenTasksId(id_)

    task = sqla_createtaskdatabase.Task.getTask(id_)

    if (len(l) == 0):

        return calculateProgressLowestChild(id_,status,duration)

    else:

        return calculateProgressChild(id_,status,duration)

def calculateProgressLowestChild(id_,status,duration):
        print("calculating progress of lowest child:",id_)
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

def calculateProgressChild(id_,status,duration):
    print("calculating progress of child:",id_)
    l = sqla_createtaskdatabase.Task.getAllChildrenTasksId(id_)


    if(status == 'finished'):

        return 1.0, duration

    else:
        sub_duration = 0
        for child_id in l:

            child_task = sqla_createtaskdatabase.Task.getTask(child_id)

            tup = calculateProgressDownTree(child_id,child_task.status,child_task.duration)
            print(tup)


            sub_duration += tup[1]*tup[0]

        task = sqla_createtaskdatabase.Task.getTask(id_)
        progress = round(sub_duration/duration,2)
        print(progress,duration,id_)
        task.progress = progress
        sqla_createtaskdatabase.Task.updateTask(task)
        print(progress, duration)
        return progress,duration

def calculateProgressParent(id_status,duration):
    pass


