from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from screenmanager import screen_manager


class TaskApp(App):

    def build(self):
        return  screen_manager()



if __name__ == '__main__':
    TaskApp().run()