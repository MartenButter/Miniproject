__author__ = 'Ashwin Bakker - 1683836'

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder


Builder.load_file('menubar.kv')

class MenuBar(BoxLayout):
    app = App()

    def create_task_screen(self,BuildID):

        self.app.BiD = BuildID
        print(BuildID, 'buildid')
        self.app.getTaskScreen(self)


    def build(self):
        pass


