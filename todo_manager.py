import argparse
from modules import ToDo
# from modules import ListManager

# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('action', help='add', nargs=2, choices=['a', 'e'])
# args = parser.parse_args()
# print(args)

myList = ToDo()
myList.loadFromStorage()
myList.add('myTodo01')
myList.add('myTodo02')
myList.add('myTodo03')
myList.add('myTodo04')
myList.edit(0, 'nuovo titolo')
myList.toggleDone(0)
print(myList.list)

# myList.saveToStorage()