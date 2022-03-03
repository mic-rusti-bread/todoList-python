from datetime import datetime


class To_do:
    def __init__(self, titolo):
        self.titolo = titolo
        # self.timestamp = datetime.timestamp(datetime.now()) 
        self.done = False
    def __str__(self):
        return "string shown to users (on str and print)"
    def __repr__(self):
        return "string shown to developers (at REPL)"        
myList = []
myList.append(To_do('myTodo01'))
myList.append(To_do('myTodo02'))
myList.append(To_do('myTodo03'))
myList.append(To_do('myTodo04'))
print(myList)
