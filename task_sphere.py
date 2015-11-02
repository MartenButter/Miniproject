from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('task_sphere.kv')

class TaskSphere(Widget):
    pass

class SphereApp(App):
    def build(self):
        return TaskSphere()

if __name__ =='__main__':
    SphereApp().run()

