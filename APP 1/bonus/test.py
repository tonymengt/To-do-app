# import FreeSimpleGUI as sg

# # label1 = sg.Text('Enter feet')
# # input1 = sg.Input()
# # label2 = sg.Text('Enter inches')
# # input2 = sg.Input()
# # button = sg.Button('Convert')

# # window = sg.Window('Convertor', layout=[[label1, input1], [label2, input2], [button]])

# button_labels = ('add', 'edit', 'apply')

# layout = []
# for label in button_labels:
#     layout.append([sg.Button(label)])

# window = sg.Window('test', layout=layout)

# window.read()
# window.close()



# import FreeSimpleGUI as sg
# from convert14 import convert 

# feet_label = sg.Text('Enter Feet')
# feet_input = sg.Input(key='feet')
# inches_label = sg.Text('Enter Inches')
# inches_input = sg.Input(key='inches')

# button = sg.Button('Convert')
# output_text = sg.Text(key='output')
# output2 = sg.Text(key='output2')

# window = sg.Window('Convertor', layout=[[feet_label, feet_input], [inches_label, inches_input], [button, output_text], [output2]])

# while True:
#     event, values = window.read()
#     if event == 'Convert':
#         final = convert(float(values['feet']), float(values['inches']))
#         output_text.update(value=f"{final} m")
#         window['output2'].update(value=f"{final} m")
#     else:
#         break

# window.close()



import FreeSimpleGUI as sg

# Define the default text
default_text = "Type here..."

layout = [
    [sg.Text("Enter your todo item:")],
    [sg.InputText(default_text=default_text, tooltip="Enter todo", key="kms")],
    [sg.Button("Submit")]
]

window = sg.Window("Input Box with Default Text and Tooltip", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    # Clear default text when the input box gains focus or is clicked
    if event == "kms" and values["kms"] == default_text:
        window["kms"].update("")

    elif event == "Submit":
        input_text = values["kms"]
        if input_text == default_text or input_text == "":
            sg.popup("Please enter a todo item.")
        else:
            print("Input Text:", input_text)

window.close()


