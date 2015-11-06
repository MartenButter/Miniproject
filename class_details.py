from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
# from kivy.graphics import Color
from sqla_createtaskdatabase import Task

# Builder.load_file('details.kv')

class Details(BoxLayout):
    # def build(self):
    #     layout = BoxLayout(orientation='vertical')
    #     layout.add_widget(Label(text='Test Label'))
    #     return self

    def test(id):
        task = Task.getTask(id)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Name:'))
        layout.add_widget(Label(text=task.name))
        description = task.description
        if description == None:
            layout.add_widget(Label(text='Description:'))
            layout.add_widget(Label(text='No Description Available'))
        else:
            layout.add_widget(Label(text='Description:'))
            layout.add_widget(Label(text=task.description))
        duration = str(task.duration) + ' uur'
        layout.add_widget(Label(text='Duration:'))
        layout.add_widget(Label(text=duration,))
        layout.add_widget(Label(text='Status:'))
        layout.add_widget(Label(text=task.status))
        progress = str(task.progress * 100) + '%'
        layout.add_widget(Label(text='Progress:'))
        layout.add_widget(Label(text=progress))
        return layout

    def update(tskID):
        Details.test(tskID)