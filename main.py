from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from TreeView import TreeView,populate_tree_view,CustomTreeView
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from sqla_createtaskdatabase import Task
from class_details import Details
from class_menubar import MenuBar
from class_task_add import AddTaskScreen

class TaskApp(App):
    detailsID = 0
    BiD = 0
    taskId = 0

    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.menuBar = MenuBar()
        self.menuBar.app = self
        self.layout.add_widget(self.menuBar)
        self.sublayout = BoxLayout(orientation='horizontal')
        self.layout.add_widget(self.sublayout)
        self.tv = CustomTreeView(root_options=dict(text='Tree One'), hide_root=True, indent_level=4)
        self.tv.size_hint = 1, None
        self.tv.bind(minimum_height = self.tv.setter('height'))
        self.tv.app = self
        populate_tree_view(self.tv)
        self.sv = ScrollView()
        self.sv.add_widget(self.tv)
        self.sublayout.add_widget(self.sv)
        # subsublayout = GridLayout()
        if self.detailsID != 0:
            self.details = Details.giveDetailsObject(self.detailsID)
            self.sublayout.add_widget(self.details)
        else:
            self.details = BoxLayout(orientation="vertical")
            self.sublayout.add_widget(self.details)
        # sublayout.add_widget(subsublayout)
        # sublayout.add_widget(Button(text='Test'))

        return  self.layout

    def updateDetails(self, *args):
        children = self.sublayout.children[:1]

        self.sublayout.clear_widgets(children=children)
        self.details = Details.giveDetailsObject(self.detailsID)
        self.sublayout.add_widget(self.details)

    def getTaskScreen(self,*args):
        children = self.sublayout.children[:1]
        self.sublayout.clear_widgets(children=children)
        print(self.taskId, 'taskid')
        print(self.BiD, 'buildid')
        self.details = AddTaskScreen(task=AddTaskScreen.get_rigt_task_for_task_screen(self.taskId,self.BiD), app=self)
        print("after AddTaskScreen()")
        #self.details.buildID = self.BiD
        #self.details.task = Task.getTask(self.taskId)
        #self.details.app = self
        self.sublayout.add_widget(self.details)
        print('im here')

    # def update_treeview(self,*args):
    #     children = self.sublayout.children[1:]
    #     self.sublayout.clear_widgets(children=children)
    #     self.sv.clear_widgets()
    #     self.tv = CustomTreeView(root_options=dict(text='Tree One'), hide_root=True, indent_level=4)
    #     self.tv.size_hint = 1, None
    #     self.tv.bind(minimum_height = self.tv.setter('height'))
    #     self.tv.app = self
    #     populate_tree_view(self.tv)
    #     self.sv = ScrollView()
    #     self.sv.add_widget(self.tv,index=0)
    #     self.sublayout.add_widget(self.sv)




if __name__ == '__main__':
    TaskApp().run()