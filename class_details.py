from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
# from kivy.graphics import Color

# Builder.load_file('details.kv')

class Details(Widget):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Test Label'))
        # return self
    def update(tskID):
        print("updated",tskID)