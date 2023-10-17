import PySimpleGUI as sg # pip install pysimplegui
import requests

if __name__ == '__main__':
    sg.theme('Default1')
    layout = [[sg.Text('Calculator')],      
                 [sg.InputText()],
                 [sg.InputText()],
                 [sg.Submit( bind_return_key=True)],
                 [sg.Text("Resultado: ", key='-RESULTADO-')]]

window = sg.Window('Actividad 8', layout)
url = 'http://127.0.0.1:6660//api_sum.php'
# Para usar este programa, el archivo api_sum.php debe estar corriendo en el servidor local en el puerto 6660


while True:
    event, values = window.read()
    if event == 'Submit':
        numero1 = values[0]
        numero2 = values[1]
        try :
            numero1 = float(numero1)
            numero2 = float(numero2)
        except:
            window['-RESULTADO-'].update('Error')
            continue
        if numero1 is not None and numero2 is not None:
            params = {'num1': numero1, 'num2': numero2}
            response = requests.get(url, params=params)
            window['-RESULTADO-'].update(response.text)
        else:
            window['-RESULTADO-'].update('Error')
    if event == sg.WIN_CLOSED:
        window.close()
        break