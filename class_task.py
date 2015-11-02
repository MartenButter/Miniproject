import sqlite3
import myfunctions

class task():

    def __init__(self,id,name,done,description,parent,duration,status,responsible_person,executer,deadline):
        self.i =        id
        self.n =        name
        self.don =      done
        self.des =      description
        self.par =      parent
        self.dur =      duration
        self.stat =     status
        self.resp =     responsible_person
        self.ex =       executer
        self.dead =     deadline

    def set_name(self,name):
        self.n =        name
    def set_done(self,done):
        self.don =      done
    def set_description(self, description):
        self.des =      description
    def set_parent_task(self,parent ):
        self.par =      parent
    def set_duration(self,duration):
        self.dur =      duration
    def set_status(self,status):
        self.stat =     status
    def set_responsible_person(self,responsible_person):
        self.resp =     responsible_person
    def set_executer(self, executer):
        self.ex =       executer
    def set_deadline(self,deadline):
        self.dead =     deadline
    def new_task_to_tuple(self):
        return (self.n,self.don, self.des ,self.par ,self.dur ,self.stat,self.resp,self.ex ,self.dead)
    def update_task(self):
        pass