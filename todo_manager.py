import argparse
from modules import ToDo

#init vars
myList = ToDo()
parser = argparse.ArgumentParser(prog='todo_manager')

#set args
parser.add_argument("-ls", '--list', action="store_true")
parser.add_argument("-a", '--add', nargs=1, type=str)
parser.add_argument("-e", '--edit', nargs=2)
parser.add_argument("-d", '--delete', nargs=1, type=int)
parser.add_argument("-t", '--toggle', nargs=1, type=int)
parser.add_argument("-s", '--search', nargs=1, type=str)

# parser.add_argument("title", help="echo the string you use here", type=str)
args = parser.parse_args()
returnValue = ''
#case decision
if args.add:
    returnValue = myList.add(args.add[0])

elif args.edit:    
    try:    
        i = int(args.edit[0])
        myList.edit(i, args.e[1])
    except:
        print('si errore')

elif args.delete:
    returnValue = myList.remove(args.delete[0])    

elif args.toggle:
    returnValue = myList.toggleDone(args.toggle[0])        

elif args.search:
    returnValue = myList.searchByTitle(args.search[0])

elif args.list:
    returnValue = myList.getList()

if returnValue : print(returnValue)
#salvo
myList.saveToStorage()