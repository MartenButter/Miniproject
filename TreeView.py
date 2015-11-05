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
from sqla_createtaskdatabase import *

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

    #HIER WORDT NIETS GEPRINT
    #Als je dB.test.py runt komt er wel gewoon een output
    #WAAROM?
    for taskName in session.query(Task.name):
        print(str(taskName))

    #Dit wordt dan weer wel geprint
    print("test")

    # for taskName in session.query(Task.name):
    #     print(taskName)

    # for task in tasks:
    #     tv.add_node(TreeViewLabel(text=task[0]))

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