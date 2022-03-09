from datetime import datetime
from fileinput import filename
import json
# from nis import cat
import pickle

class Activity:
    ##for future updates
    # si potrebbero usare i setter e getter del property() ma dopo sul json di __repr__ vengono gli attributi con davanti l'underscore (es. _titolo)
    # da capire melgio
    # self.title_validated = title
    # title_validated=property(getTitle, setTitle)


    def __init__(self, title, id=0):
        self.id = id
        self.setTitle(title)
        self.timestamp = datetime.timestamp(datetime.now()) 
        self.done = False

    def setTitle(self, value, validate = True):
        if validate:
            if len(value) < 5:
                raise ValueError("Title too short. Must be longer than 5 characters")
        self.title = value
        
    def getTitle(self):
        return self.title

    def setToggleDone(self):
        self.done = not self.done

    def __repr__(self): 
        return json.dumps(self.__dict__)
    


class ToDo:
    ##for future updates
    # Right now all the 'searchById' is made bruteforcing the list, if the project scale up, we could implement a dictionary to map all the ids to the relative postion in the array
    # same concept could apply to the 'searchByName'

    def __init__(self, in_storageFile=''):
        self.list = []
        self.storageFile = in_storageFile
        if self.storageFile != '':
            self.loadFromStorage()

    def getList(self, orderBy, in_reverse=False):
        return sorted(self.list, key=lambda activity: getattr(activity, orderBy), reverse=in_reverse)

    def loadFromStorage(self, in_storageFile =''):
        #Mi potrebbe specificare di fare il load da un altro file
        filename = self.storageFile
        if in_storageFile != '':
            filename = in_storageFile

        try:
            file = open(filename,"rb") 
            self.list = pickle.load(file)
        except FileNotFoundError:
            self.list = []
  
    def saveToStorage(self, in_storageFile =''):  
        #Mi potrebbe specificare di fare la save da un altro file
        filename = self.storageFile
        if in_storageFile != '':
            filename = in_storageFile   

        with open(filename, 'wb') as file:
            pickle.dump(self.list, file)


    def add(self, title):
        id = 0 #lo metto qui perchè è un progressivo della tabella
        
        lengthList = len(self.list)
        if lengthList > 0:
            id = self.list[lengthList - 1].id + 1         # aggiungo 1 al numero di index mssimo contenuto visto che potrebbe non corrispondere alla lunghezza della list

        try:
            newActivity = Activity(title, id)
            self.list.append(newActivity)
        except ValueError as err:
            return 'Validation error:\n ' + str(err)

    def editTitle(self, id, newTitle):
        obj = self.searchById(id)
        if not obj:
            return "id not found"

        try:
            self.list[obj.id].setTitle(newTitle)
        except ValueError as err:
            return 'Validation error:\n ' + str(err)

    def remove(self, id):
        obj = self.searchById(id)
        if not obj:
            return "id not found"

        self.list.remove(obj) 


    def toggleDone(self, id):
        obj = self.searchById(id)
        if not obj:
            return "id not found"

        self.list[obj.id].setToggleDone()


    def searchByTitle(self, titleToSearch):
        returnList = []
        titleToSearch = titleToSearch.lower()

        for elem in self.list:
            if titleToSearch in elem.getTitle().lower():
                returnList.append(elem)
        return returnList

    def searchById(self, id):
        for elem in self.list:
            if id == elem.id:
                return elem
        return False    
    