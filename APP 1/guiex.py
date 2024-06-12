from modules import functions
import FreeSimpleGUI as sg
import time

sg.theme('black')
clock = sg.Text('', key= 'clock')
label = sg.Text('Type in a to do')
input_box = sg.InputText(tooltip='Enter todo', key = 'todo')
add_button = sg.Button(image_source="APP 1/picture/add.png", mouseover_colors='LightBlue2', tooltip='Add', key='Add')
list_box = sg.Listbox(values= functions.get_todos(), key = 'todos',
                      enable_events=True, size = [45, 10])
edit_button = sg.Button('Edit')
complete_btn = sg.Button('Complete')
exit_btn = sg.Button('Exit')


window = sg.Window('My to do app', 
                   layout=[[clock],
                           [label], 
                           [input_box, add_button], 
                           [list_box, edit_button, complete_btn],
                           [exit_btn]], 
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)

    if event in(sg.WIN_CLOSED, "Exit"):
        break
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an existing task first", font=("Helvetica", 20))
        case "Complete":
            try:
                comp = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(comp)
                # index = todos.index(comp)
                # todos.pop(index)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value= '')
            except IndexError:
                sg.popup("Please select an existing task first", font=("Helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value= values['todos'][0])
        case sg.WIN_CLOSED:
            break # the exit() statement will complete close the program while the break will only exit the while statement

# you can assign two variables for tuples and list using x,y = (1,2) output x= 1, y = 2
window.close()