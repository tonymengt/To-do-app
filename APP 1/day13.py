# set default paramater. doing so will reduce the number of static/hard coded paramter.

def get_todos(filepath = 'APP 1/todos.txt'):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

# when working with multiple paramters, the defail parameter need to placed at the end
def write_todos(todos_arg, failpath = 'APP 1/todos.txt'):
    with open(failpath, 'w') as file:
        file.writelines(todos_arg)

while True: 
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()


    if user_action.startswith('add'):

        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)
        
    elif user_action.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item.capitalize()}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            
            todos = get_todos()

            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print('Your Command is not valid.')
            continue

    elif user_action.startswith('complete'):
        try:
            complete = int(user_action[9:])

            todos = get_todos()

            index = complete - 1
            to_be_removed = todos[index]
            todos.pop(index)

            write_todos(todos)

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