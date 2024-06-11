FILEPATH = 'APP 1/todos.txt'

def get_todos(filepath = FILEPATH):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

# when working with multiple paramters, the defail parameter need to placed at the end
def write_todos(todos_arg, failpath = FILEPATH):
    with open(failpath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("hello from functions")