__author__ = 'Ashwin Bakker - 1683836'
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.treeview import TreeView, TreeViewNode
from kivy.uix.treeview import TreeViewLabel
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.button import Button
import sqla_createtaskdatabase

# import sqlite3

# conn = sqlite3.connect('C:/Users/Ashwin/OneDrive/HU/Programming - TICT-V1PROG-15/Miniproject Programming/task_database.db')
# cur = conn.cursor()

# modGroups = [u'Fruit', u'Fruit', u'Meat', u'Dairy', u'Dairy', u'Fruit']
# modItems = [u'Apple', u'Pear', u'Spam', u'Egg', u'Milk', u'Banana']
# modDict = dict()
# modDictUnique = dict()

class TreeViewButton(Button, TreeViewNode):
    pass

def populate_tree_view(tv):

    def getAllParentTasksId():
        parentId = []
        for instance in sqla_createtaskdatabase.session.query(sqla_createtaskdatabase.Task).\
                filter(sqla_createtaskdatabase.Task.task_id==None):
            parentId.append(instance.id)
        #Returns them in a list
        return parentId

    def getParentTaskNames():

        names = []
        for name in sqla_createtaskdatabase.session.query(sqla_createtaskdatabase.Task.name).\
                    filter(sqla_createtaskdatabase.Task.task_id==None):
            names.append(name[0])
        return names

    def getChildTaskNames(parentId):
        childId = []
        for instance in sqla_createtaskdatabase.session.query(sqla_createtaskdatabase.Task).\
                filter(sqla_createtaskdatabase.Task.task_id==parentId):
            childId.append(instance.id)


    taskNames = getParentTaskNames()
    for task in taskNames:
        tv.add_node(TreeViewLabel(text=task))

    # for taskName in sqla_createtaskdatabase.session.query(sqla_createtaskdatabase.Task.name).\
    #             filter(sqla_createtaskdatabase.Task.task_id==None):
    #     tv.add_node(TreeViewLabel(text=taskName[0]))

    # tasks = []

    # for taskName in sqla_createtaskdatabase.session.query(sqla_createtaskdatabase.Task.name):
    #     tasks.append(taskName[0])

    # for task in tasks:
    #     tv.add_node(TreeViewLabel(text=task))



    # tv.add_node(TreeViewLabel(text='Podium'),n1)

    # modDict = zip(modGroups, modItems)
    # print(modGroups)
    # print(modItems)
    # for k, v in modDict:
    #     if k not in modDictUnique:
    #         modDictUnique[k] = [v]
    #     else:
    #         modDictUnique[k].append(v)
    # sortedGroups = modDictUnique.keys()
    # sortedGroups.sort()
    #print modItems
    #print modDictUnique
    # n = tv.add_node(TreeViewLabel(text='Food', is_open=True))
    # for group in sortedGroups:
    #     g = tv.add_node(TreeViewLabel(text='%s' % group), n)
    #     for item in modDictUnique[group]:
    #         tv.add_node(TreeViewButton(text='%s' % item), g)

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

# conn.close()