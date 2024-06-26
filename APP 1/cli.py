
# from function14 import get_todos, write_todos
from modules import functions #if this method is used, function14 needs to be referenced when using functions within the function14 file. i.e. function14.get_todos()
# use from "name of directory" if the function file is stored within another directory.
import time 

# Glob module, this allows you to look for specific file type.

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True: 
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()


    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)
        
    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item.capitalize()}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            
            todos = functions.get_todos()

            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print('Your Command is not valid.')
            continue

    elif user_action.startswith('complete'):
        try:
            complete = int(user_action[9:])

            todos = functions.get_todos()

            index = complete - 1
            to_be_removed = todos[index]
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {to_be_removed.strip('\n')} was removed from the list."
            print(message)
        except IndexError:
            print('There is no item with that command')
            continue

    elif user_action.startswith('exit'):
        break
    else:
         print("you entered an unrecognized command.")

print("Bye")