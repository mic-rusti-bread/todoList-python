from datetime import datetime
import json
class Activity:
    def __init__(self, titolo):
        self.titolo = titolo
        self.timestamp = datetime.timestamp(datetime.now()) 
        self.done = False

    def __repr__(self): 
        return json.dumps(self.__dict__)


#Che questa diventi ToDo dalla quale gestire tutto?
#Potrebbe non essere più generica ma una collection diretta di activity
#A questo punto 
class ListManager:
    def __init__(self):
        self.list = []

    def add(self, obj):
        self.list.append(obj)

    def remove(self, index):
        return self.list.pop(index)
    
    def edit(self, index, newTitle):
        self.list[index].title = newTitle

    def toggleTrueFalse(self, index, pty):
        self.list[index][pty] = not self.list[index][pty]

    def search():
        #cerca in lista
        #ritorna oggetto singolo
        pass 