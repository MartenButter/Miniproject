from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file("buildstring_screenmanager.kv")

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass
class TaskDetailsScreen(Screen):
    pass
# Create the screen manager
def screen_manager():
    sm = ScreenManager()
    sm.add_widget(MenuScreen(name='menu'))
    sm.add_widget(SettingsScreen(name='settings'))
    sm.add_widget(TaskDetailsScreen(name='taskdetails'))
    return sm

