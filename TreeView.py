__author__ = 'Ashwin Bakker - 1683836'

from kivy.uix.scrollview import ScrollView
# from kivy.uix.gridlayout import GridLayout
# from kivy.core.window import Window
# from kivy.uix.widget import Widget
from kivy.uix.treeview import TreeView, TreeViewNode
from kivy.uix.treeview import TreeViewLabel
from kivy.app import App
# from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.button import Button
from kivy.lang import Builder
import sqla_createtaskdatabase
from sqla_createtaskdatabase import *

Builder.load_file('BoomMakeup.kv')

class TreeViewButton(Button, TreeViewNode):
    def test(self):
        print('Test')

def populate_tree_view(tv):

    # n = tv.add_node(TreeViewLabel(text='Tasks', is_open=True))

    def CreateTree(tv):
        parentIDS = Task.getAllParentTasksAndId()
        lst = []
        for ID in parentIDS:
            tvl = TreeViewButton(text=parentIDS[ID].name)
            print('CreateParentNode')
            n = tv.add_node(tvl)
            CreateChildNodes(tv, ID, n)


    def CreateChildNodes(tv, parentID, n):
        childrenDCT = Task.getAllChildrenTasksAndId(parentID)
        if len(childrenDCT) == 0:
            print('return')
            return
        else:
            for child in childrenDCT:
                print(child)
                tvl = TreeViewButton(text=childrenDCT[child].name)
                g = tv.add_node(tvl,n)
                tvl = CreateChildNodes(tv, child,g)



    def getParentTaskNames():
        names = []
        for name in sqla_createtaskdatabase.session.query(sqla_createtaskdatabase.Task.name).\
                    filter(sqla_createtaskdatabase.Task.task_id==None):
            names.append(name[0])
        return names

    def getChildTaskNames(parentId):
        childName = []
        for name in sqla_createtaskdatabase.session.query(sqla_createtaskdatabase.Task).\
                filter(sqla_createtaskdatabase.Task.task_id==parentId):
            childName.append(name.name)
        return childName

    def addNodes():
        parentNames = getParentTaskNames()
        for name in parentNames:
            g = tv.add_node(TreeViewLabel(text=name))
        childNames = []
        for id in Task.getAllParentTasksId():
            childNames.append(getChildTaskNames(id))

        # for child in (childNames[0][:]+childNames[1][:]):
        #     tv.add_node(TreeViewButton(text=child), g)
        # # print(childNames[0][:]+childNames[1][:])

    CreateTree(tv)

    # addNodes()

class TreeViewApp(App):

    def build(self):
        #for i in range(30):
        #    btn = Button(text=str(i), size=(480, 40),
        #                 size_hint=(None, None))
        #    layout.add_widget(btn)
        tv = TreeView(root_options=dict(text='Tree One'), hide_root=True, indent_level=4)
        tv.size_hint = 1, None
        tv.bind(minimum_height = tv.setter('height'))
        populate_tree_view(tv)
        root = ScrollView(pos = (0, 0))
        root.add_widget(tv)
        return root

if __name__ == '__main__':
    TreeViewApp().run()
