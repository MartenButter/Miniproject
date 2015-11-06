__author__ = 'Ashwin Bakker - 1683836'
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from sqla_createtaskdatabase import Task
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ObjectProperty,NumericProperty
Builder.load_file('add_task.kv')

class AddTaskScreen(BoxLayout):
    taskId = NumericProperty()
    buildId = NumericProperty()
    task = ObjectProperty()
    app = ObjectProperty()


    def createParentTask(self,name,description,duration, deadline):

        self.task.name = name
        self.task.description = description
        self.task.duration = int(duration)
        self.task.deadline = deadline
        Task.updateTask(self.task)

        self.clear_widgets()

        print('app is running')
        popup = Popup(title='You have created a new task!',auto_dismiss=False)
        popup.size_hint = 0.25,0.25

        content = Button(text='Close me!',size_hint_y = .10)
        popup.add_widget(content)

        # bind the on_press event of the button to the dismiss function
        content.bind(on_press=popup.dismiss)
        popup.open()


    def noneToString(self,x):

        if x == None:
            return ''
        else:
            return str(x)


    def get_rigt_task_for_task_screen(taskId,buildId):
        if buildId == 0 and taskId != 0:
            task = Task.getTask(taskId)
            print('editing new parent task')
        if buildId == 1:
            task = Task()
            print('')
        if buildId == 2 and taskId != 0:
            task = Task()
            task.task_id = taskId

        return task


class AddTaskApp(App):
    taskId = 6
    def build(self):
        root = AddTaskScreen(task=Task.getTask(self.taskId))
        return root


if __name__ == '__main__':
    AddTaskApp().run()
