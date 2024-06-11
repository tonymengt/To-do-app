while True: 
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + '\n'

            # this is the recommended method to deal with files
            with open('APP 1/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)
            # you can create a new file document using the open function if the name of the file is brand new
            with open('APP 1/todos.txt', 'w') as file:
                file.writelines(todos)
            
        case "show" | "display ":
            with open('APP 1/todos.txt', 'r') as file:
                todos = file.readlines()
            
            # new_todos = []

            # for item in todos:
            #     new_items = item.strip('\n')
            #     new_todos.append(new_items)

            # list comprihension - inline for loop
            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item.capitalize()}"
                print(row)
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            
            with open('APP 1/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('APP 1/todos.txt', 'w') as file:
                file.writelines(todos)
            
        case "complete":
            complete = int(input("number of the todo to complete: "))

            with open('APP 1/todos.txt', 'r') as file:
                todos = file.readlines()

            index = complete - 1
            to_be_removed = todos[index]
            todos.pop(index)

            with open('APP 1/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {to_be_removed.strip('\n')} was removed from the list."
            print(message)
        case "exit":
            break
        case _:
            print("you entered an unrecognized command.")

print("Bye")