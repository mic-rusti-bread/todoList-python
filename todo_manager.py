import argparse
from modules import ToDo

#init vars
todo_list_manager = ToDo('storagePersist.txt')
parser = argparse.ArgumentParser(prog='todo_manager')
returnValue = None 

#set args
parser.add_argument("-ls", '--list', action="store_true", help='Lists all values ordered by desc(timestamp)')
parser.add_argument("-a", '--add', nargs=1, type=str, help="Adds a new activity. --> Pass ['newTitle'] as param. Must be longer than 5 chars")
parser.add_argument("-e", '--edit', nargs=2, help = "Edits an existing activity. --> Pass ['id'] and ['new Title'] as params")
parser.add_argument("-d", '--delete', nargs=1, type=int, help="Deletes an existing activity. --> Pass ['id'] as param")
parser.add_argument("-t", '--toggle', nargs=1, type=int, help="Toggles ['done'] true/false of an existing activity. --> Pass ['id'] as param")
parser.add_argument("-s", '--search', nargs=1, type=str, help="Searches and existing activity --> Pass ['id'] as param")
args = parser.parse_args()



if args.add:
        todo_list_manager.add(args.add[0])

elif args.edit:    
    try:    
        i = int(args.edit[0])
        todo_list_manager.editTitle(i, args.edit[1])
        
    except ValueError:
        returnValue = 'Value of argument(/s) unexpected, refer to [-h | --help] for more information '
    except IndexError as err:
        returnValue = "Index Error: " + str(err)

elif args.delete:
    try:
        todo_list_manager.remove(args.delete[0])    
    except IndexError as err:
        returnValue = "Index Error: " + str(err)

elif args.toggle:
    try:
        todo_list_manager.toggleDone(args.toggle[0])        
    except IndexError as err:
        returnValue = "Index Error: " + str(err)

elif args.search:
    returnValue = todo_list_manager.searchByTitle(args.search[0])

elif args.list:
    returnValue = todo_list_manager.getList('id', True)


if returnValue != None: print(returnValue)

#salvo
todo_list_manager.saveToStorage()



