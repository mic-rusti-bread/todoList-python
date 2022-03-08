from datetime import datetime
import json
import pickle

class Activity:
    def __init__(self, titolo, id=''):
        self.id = id
        self.titolo = titolo
        self.timestamp = datetime.timestamp(datetime.now()) 
        self.done = False

    def getTitle(self):
        return self.titolo

    def setTitle(self, nuovoTitolo):
        self.titolo = nuovoTitolo

    def setToggleDone(self):
        self.done = not self.done

    def __repr__(self): 
        return json.dumps(self.__dict__)



class ToDo:
    def __init__(self):
        self.list = []
        self.loadFromStorage()

    def getList(self):
        return self.list

    def loadFromStorage(self):
        file = open("localPersist.txt","rb") 
        try:
            self.list = pickle.load(file)
        except:
            self.list = []
  
    def saveToStorage(self):       
        with open('localPersist.txt', 'wb') as file:
            pickle.dump(self.list, file)


    def add(self, titolo):
        if len(titolo) < 5:
            return 'Titolo troppo corto'

        #lo metto qui perche voglio che sia un progressivo
        id = 0

        # aggiungo 1 al numero di index massimo contenuto visto che potrebbe non corrispondere alla lunghezza della list
        lengthList = len(self.list)
        if lengthList > 0:
            id = self.list[lengthList - 1].id + 1           

        newActivity = Activity(titolo, id)
        self.list.append(newActivity)

    def remove(self, id):
        obj = self.searchById(id)
        if obj:
            return "not found"
        
        self.list.remove(obj)    

    def edit(self, id, newTitle):
        obj = self.searchById(id)
        if not obj :
            return "not found"
        
        self.list[obj.id].setTitle(newTitle)

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
    
    def validate(self, id, titolo, ):
        pass



##Appunti
#Aggiungere validazione, non so se nella classe del ToDo o nel modello
#Nel modello starebbe male perche ci sono solo le cose dell'oggetto ma potremmo metterci   
#il salvataggio a db direttamente. In questo modo abbiamo una divisione effettiva
#tra chi interagisce con i dati e chi li mette a db. 