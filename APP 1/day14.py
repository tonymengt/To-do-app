
# from function14 import get_todos, write_todos
from modules import function14 #if this method is used, function14 needs to be referenced when using functions within the function14 file. i.e. function14.get_todos()
# use from "name of directory" if the function file is stored within another directory.
while True: 
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()


    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = function14.get_todos()

        todos.append(todo + '\n')

        function14.write_todos(todos)
        
    elif user_action.startswith('show'):
        todos = function14.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item.capitalize()}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            
            todos = function14.get_todos()

            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'

            function14.write_todos(todos)

        except ValueError:
            print('Your Command is not valid.')
            continue

    elif user_action.startswith('complete'):
        try:
            complete = int(user_action[9:])

            todos = function14.get_todos()

            index = complete - 1
            to_be_removed = todos[index]
            todos.pop(index)

            function14.write_todos(todos)

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