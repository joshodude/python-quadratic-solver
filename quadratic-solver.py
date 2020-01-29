import PySimpleGUI as sg
import quadmath

sg.theme('Dark')
sg.SetOptions(element_padding=(0, 0), margins=(10, 0), font=('Tahoma', 18))


nostrings = [[sg.Text('This program only accepts numbers.')]]

inputcol = [[sg.Text('Input:', font=('Tahoma', 20), pad=(0, 10))],
            [sg.Text('Enter A:', size=(7, 1)), sg.InputText(size=(6, 1), do_not_clear=False, key='a')],
            [sg.Text('Enter B:', size=(7, 1)), sg.InputText(size=(6, 1), do_not_clear=False, key='b')],
            [sg.Text('Enter C:', size=(7, 1)), sg.InputText(size=(6, 1), do_not_clear=False, key='c')]]

answercol = [[sg.Text('Output:', font=('Tahoma', 20), pad=(0, 10))],
             [sg.Text('Discriminant:', size=(12, 1)), sg.Text('', size=(20, 1), key='d')],
             [sg.Text('Solution:', size=(12, 1)), sg.Text('', size=(20, 1), key='solution')],
             [sg.Text('', size=(12, 1)), sg.Text('', size=(20, 1), key='solution2')]]

answercol2 = [[sg.Text('', font=('Tahoma', 20), pad=(0, 10))],
             [sg.Text('Standard:', size=(10, 1)), sg.Text('', size=(20, 1), key='standard')]]

layout = [[sg.Column(inputcol), sg.Column(answercol), sg.Col(answercol2)],
          [sg.Button('Cancel', button_color=('white', 'red'), pad=(10, 20)),
           sg.Button('Calculate', button_color=('white', 'green'), pad=(0, 20))]]


window = sg.Window('Python Quadratic Solver', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        tryA = int(values['a']) + 1
        tryB = int(values['b']) + 1
        tryC = int(values['c']) + 1

        solution = quadmath.TheMath(values['a'], values['b'], values['c']).calc_zeros()

        discriminant = ((int(values['b']) ** 2) - (4 * int(values['a']) * int(values['c'])))
        window.FindElement('d').update(discriminant)

        window.FindElement('standard').update(quadmath.TheMath(values['a'], values['b'], values['c']).convrt_vertex())

        if 'X =' in solution[0]:
            window.FindElement('solution').update(solution[0])
            window.FindElement('solution2').update(solution[1])
        else:
            window.FindElement('solution').update(solution)
            window.FindElement('solution2').update('')

    except ValueError:
        confirm = sg.PopupOK('This program only accepts numbers.', title='Error', button_color=('white', 'green'))
        window.FindElement('d').update('')
        window.FindElement('solution').update('')
        window.FindElement('solution2').update('')

window.close()