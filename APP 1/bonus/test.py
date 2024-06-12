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



import FreeSimpleGUI as sg
from convert14 import convert 

sg.theme('black')
feet_label = sg.Text('Enter Feet')
feet_input = sg.Input(key='feet')
inches_label = sg.Text('Enter Inches')
inches_input = sg.Input(key='inches')

button = sg.Button('Convert')
output_text = sg.Text(key='output')
output2 = sg.Text(key='output2')
exit_btn = sg.Button("Exit")
window = sg.Window('Convertor', layout=[[feet_label, feet_input], [inches_label, inches_input], [button,exit_btn, output_text]])

while True:
    event, values = window.read()
    if event == 'Convert':
        try:
            final = convert(float(values['feet']), float(values['inches']))
            output_text.update(value=f"{final} m")
            window['output2'].update(value=f"{final} m")
        except ValueError:
            sg.popup('Please enter values for feet and inches')
    elif event == 'Exit':
        break
    else:
        break
window.close()


