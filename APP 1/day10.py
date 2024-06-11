# striping the match and case operator and replace it with the if and in operator to remove additional steps within the function.

while True: 
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()


    if user_action.startswith('add'):
        # we don't need to use to enter the todo since it was already implied within the initial add commend
        # we are performing a array slicing to remove the add string and only incorporate the actual action
        todo = user_action[4:]
        # this is the recommended method to deal with files
        with open('APP 1/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')
        # you can create a new file document using the open function if the name of the file is brand new
        with open('APP 1/todos.txt', 'w') as file:
            file.writelines(todos)
        
    elif user_action.startswith('show'):
        with open('APP 1/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1} - {item.capitalize()}"s
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            
            with open('APP 1/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('APP 1/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print('Your Command is not valid.')
            continue

    elif user_action.startswith('complete'):
        try:
            complete = int(user_action[9:])

            with open('APP 1/todos.txt', 'r') as file:
                todos = file.readlines()

            index = complete - 1
            to_be_removed = todos[index]
            todos.pop(index)

            with open('APP 1/todos.txt', 'w') as file:
                file.writelines(todos)

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