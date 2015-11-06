from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from TreeView import TreeView,populate_tree_view
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from sqla_createtaskdatabase import Task
from class_details import Details

class TaskApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Button(text='Hello 1',size_hint=(1,0.2)))
        sublayout = BoxLayout(orientation='horizontal')
        layout.add_widget(sublayout)
        tv = TreeView(root_options=dict(text='Tree One'), hide_root=True, indent_level=4)
        tv.size_hint = 1, None
        tv.bind(minimum_height = tv.setter('height'))
        populate_tree_view(tv)
        sv = ScrollView()
        sv.add_widget(tv)
        sublayout.add_widget(sv)
        # subsublayout = GridLayout()
        sublayout.add_widget(Details())
        # sublayout.add_widget(subsublayout)
        # sublayout.add_widget(Button(text='Test'))

        return  layout



if __name__ == '__main__':
    TaskApp().run()