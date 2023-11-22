import PySimpleGUI as sg
from v3_json import get_json
from PIL import Image


VisualStudioCode = get_json()
k = 0   #Счётчик для закрашивания кнопки "Ввод" при её нажатии в серый и возвращения в первоначальный цвет при нажатии кнопки "Ещё раз".

def function():
    """Эта функция выводит JSON при вводе репозитория по имени:VisualStudioCode"""
    if k == 0:
        if values['-IN-'] == 'VisualStudioCode':
            window['OUT1'].Update(VisualStudioCode['company'])
            window['OUT2'].Update(VisualStudioCode['created_at'])
            window['OUT3'].Update(VisualStudioCode['email'])
            window['OUT4'].Update(VisualStudioCode['id'])
            window['OUT5'].Update(VisualStudioCode['name'])
            window['OUT6'].Update(VisualStudioCode['url'])
        else:
            window['-IN-'].Update('Введите правильное имя репозитория!Подсказка:VisualStudioCode')

def function_2():
    """Эта функция очищает окна вводы и вывода данных."""
    window['-IN-'].Update('')
    window['OUT1'].Update('')
    window['OUT2'].Update('')
    window['OUT3'].Update('')
    window['OUT4'].Update('')
    window['OUT5'].Update('')
    window['OUT6'].Update('')
    window['Ввод'].update(button_color=('azure2'))


sg.theme('DarkTeal6')
font = ("Comic Sans MS", 20)    #Шрифт заголовка
font_2 = ("Comic Sans MS", 17)  #Шрифт основного текста
layout = [[sg.Text('Получение JSON', font=font)],
        [sg.Text('Ввод имени репозитория', size=(22, 1), font=font_2), sg.InputText(key='-IN-', size=(48, 1), font=font_2)],
        [sg.Button('Ввод', font=font_2), sg.Button('Ещё раз', font=font_2), sg.Button('Отмена', font=font_2)],
        [sg.Text('company', size=(22, 1), font=font_2), sg.InputText(key='OUT1', size=(38, 1), font=font_2)],
        [sg.Text('created_at', size=(22, 1), font=font_2), sg.InputText(key='OUT2', size=(38, 1), font=font_2)],
        [sg.Text('email', size=(22, 1), font=font_2), sg.InputText(key='OUT3', size=(38, 1), font=font_2)],
        [sg.Text('id', size=(22, 1), font=font_2), sg.InputText(key='OUT4', size=(38, 1), font=font_2)],
        [sg.Text('name', size=(22, 1), font=font_2), sg.InputText(key='OUT5', size=(38, 1), font=font_2)],
        [sg.Text('url', size=(22, 1), font=font_2), sg.InputText(key='OUT6', size=(38, 1), font=font_2)],
        [sg.Image('11\Image1.png')]]

window = sg.Window('', layout, size=(1000, 700))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event =='Отмена':
        break
    if event == 'Ввод':
        function()
        k += 1
        window['Ввод'].update(button_color=('grey'))
    if event == 'Ещё раз':
        function_2()
        k = 0
window.close()

