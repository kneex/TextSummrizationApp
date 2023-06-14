import PySimpleGUI as sg
from main import pegasus_summary
from readimage import extract
from pathlib import Path

menu_layout = [
    ['File', ['Image', 'Text']]
]

layout = [
    [sg.Text('Text Summarizor')],
    [sg.Menu(menu_layout)],
    [sg.Multiline(size=(60,20), key='-IMAGE_TEXT-')],
    [sg.Button('Convert!')],
    [sg.Multiline(size=(60,20), key='-RESULT-')]
]



window = sg.Window('Text Summarization', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Convert!':
        temp =  values['-IMAGE_TEXT-']
        text_2 = pegasus_summary(temp)
        window['-RESULT-'].update(text_2)
    
    if event == 'Image':
        image_path = sg.popup_get_file('Open',no_window = True)
        text_1 = extract(image_path)
        window['-IMAGE_TEXT-'].update(text_1)
        
    if event == 'Text':
        file_path = sg.popup_get_file('open', no_window=True)
        if file_path:
            file = Path(file_path)
            window['-IMAGE_TEXT-'].update(file.read_text())


               
window.close()