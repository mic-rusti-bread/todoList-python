from datetime import datetime
import json


class Activity:
    def __init__(self, titolo):
        self.titolo = titolo
        self.timestamp = datetime.timestamp(datetime.now()) 
        self.done = False

    def getTitle(self):
        return self.titolo

    def edit(self, nuovoTitolo):
        self.titolo = nuovoTitolo

    def toggleDone(self):
        self.done = not self.done

    def __repr__(self): 
        return json.dumps(self.__dict__)



class ToDo:
    def __init__(self):
        self.list = []
    
#Quando carica, lui mette le righe come testo dentro il la lista, invece dobbiamo trasformarle in oggetto
    def loadFromStorage(self):
        file = open("localPersist.txt","r") 
        self.list = file.readlines()
        file.close()
    
    def saveToStorage(self):
        file = open("localPersist.txt","w+")
        for item in self.list:
            file.write("%s\n" % item)  
        file.close

    def add(self, titolo):
        newActivity = Activity(titolo)
        self.list.append(newActivity)

    def remove(self, index):
        return self.list.pop(index)
    
    def edit(self, index, newTitle):
        self.list[index].edit(newTitle)

    def toggleDone(self, index):
        self.list[index].toggleDone()

    def search(self, stringToSearch):
        returnList = []
        stringToSearch = stringToSearch.lower()

        for elem in self.list:
            if stringToSearch in elem.getTitle().lower():
                returnList.append(elem)

        return returnList