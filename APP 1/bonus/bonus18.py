import FreeSimpleGUI as sg
import zip 

label1 = sg.Text("Select archive:")
input1 = sg.Input()
# fileBrowse only allows a SINGLE entry. Where filesBrowse allows for multiple entries
choose_button1 = sg.FileBrowse("Choose", key='archive')

label2 = sg.Text("Select destination directory:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key='folder')

extract_button = sg.Button("Extract")
output = sg.Text(key='output', text_color='green')

window = sg.Window("File Extractor", layout=[[label1, input1, choose_button1], [label2, input2, choose_button2], [extract_button, output]])

while True:
    event, values = window.read()
    print(event,values)
    if event == 'Extract':        
        archivepath = values['archive']
        folder = values['folder']
        zip.extract_archive(archivepath, folder)
        window['output'].update(value= 'Extraction Completed')
    else:
        break
window.close()