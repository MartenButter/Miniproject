import sqlite3
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

conn = sqlite3.connect('C:/Users/Ashwin/SkyDrive/HU/Programming - TICT-V1PROG-15/Miniproject Programming/task_database.db')
cur = conn.cursor()

Builder.load_file('task_sphere.kv')

class TaskSphere(Widget):
    pass

class SphereApp(App):
    cur.execute('SELECT name FROM Tasks')
    name = cur.fetchone()
    name = str(name[0])
    def build(self):
        return TaskSphere()

if __name__ =='__main__':
    SphereApp().run()

conn.close()
