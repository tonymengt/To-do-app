import FreeSimpleGUI as sg
import zip 

label1 = sg.Text("Select files to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key='file')

label2 = sg.Text("Select destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key='folder')

compress_button = sg.Button("Compress")
output = sg.Text(key='output', text_color='green')

window = sg.Window("File Compresser", layout=[[label1, input1, choose_button1], [label2, input2, choose_button2], [compress_button, output]])

while True:
    event, values = window.read()
    print(event,values)
    filepath = values['file'].split(';')
    folder = values['folder']
    zip.make_archive(filepath, folder)
    window['output'].update(value= 'Compression Completed')

window.close()


