from datetime import datetime
import json
# from nis import cat
import pickle

class Activity:
    def __init__(self, title, id=0):
        self.id = id
        self.title = self.setTitle(title)
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


#si potrebbe aggiungere un dizionaro che tiene conto di qual
#id appartiene a quale indice nell'array per velocizzare la ricerca
#visto che al momento la property id viene considerata un identificativio e non un indice array
class ToDo:
    def __init__(self):
        self.list = []
        self.loadFromStorage()

    def getList(self, orderBy, reverseParam=False):
        return sorted(self.list, key=lambda activity: getattr(activity, orderBy), reverse=reverseParam)

    def loadFromStorage(self):
        file = open("localPersist.txt","rb") 
        try:
            self.list = pickle.load(file)
        except:
            self.list = []
  
    def saveToStorage(self):       
        with open('localPersist.txt', 'wb') as file:
            pickle.dump(self.list, file)


    def add(self, title):
        id = 0 #lo metto qui perche voglio che sia un progressivo
        # aggiungo 1 al numero di index massimo contenuto visto che potrebbe non corrispondere alla lunghezza della list
        lengthList = len(self.list)
        if lengthList > 0:
            id = self.list[lengthList - 1].id + 1           

        try:
            newActivity = Activity(title, id)
            self.list.append(newActivity)
        except ValueError as err:
            return 'Validation error:\n ' + str(err)

    def editTitle(self, id, newTitle):
        obj = self.searchById(id)
        if not obj:
            return "not found"

        try:
            self.list[obj.id].setTitle(newTitle)
        except ValueError as err:
            return 'Validation error:\n ' + str(err)

    def remove(self, id):
        obj = self.searchById(id)
        if not obj:
            return "not found"
        self.list.remove(obj)    


    def toggleDone(self, id):
        obj = self.searchById(id)
        if not obj:
            return "not found"

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
    