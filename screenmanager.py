from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
import TreeView

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_file("buildstring_screenmanager.kv")

# Declare both screens
class TaskScreen(Screen):
    def build(self):
        tv = TreeView(root_options=dict(text='Tree One'), hide_root=True, indent_level=4)
        tv.size_hint = 1, None
        tv.bind(minimum_height = tv.setter('height'))
        TreeView.populate_tree_view(tv)
        root = TreeView.ScrollView(pos = (0, 0))
        root.add_widget(tv)
        return root

class SettingsScreen(Screen):
    pass
class TaskDetailsScreen(Screen):
    pass
# Create the screen manager
def screen_manager():
    sm = ScreenManager()
    sm.add_widget(TaskScreen(name='menu'))
    sm.add_widget(SettingsScreen(name='settings'))
    sm.add_widget(TaskDetailsScreen(name='taskdetails'))
    return sm

