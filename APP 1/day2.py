#user_prompt = "Enter a todo:"

#todos = []

#while True: 
#    todo = input(user_prompt)
#    todos.append [todo]


#prompt = "enter your name "

#x = 1

#while x < 5:
#    todo = input(prompt)
#    cap = todo.capitalize()
#    print(cap)
#    x += 1

#greeting = "hello"
#print(greeting.upper())


#DAY 3 ----------------------------


todos = []

while True: 
    user_action = input("Type add or show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display ":
            for item in todos:
                print(item.capitalize())
        case "exit":
            break
        case _:
            print("you entered an unrecognized command.")

print("Bye")



