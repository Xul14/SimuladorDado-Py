# ## SIMULADOR DE DADO
# # Simular o uso de um dado gerando um valor de 1 até 6.

import random
import PySimpleGUI as sg

class SimuladorDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado? '

        sg.theme('DarkBlack')

        # Layout
        self.layout = [
            [sg.Column([
                [sg.Text('Jogar o dado?', font=('Helvetica', 20), text_color='white')]],
                justification='center')
            ],
            [sg.Column([
                [sg.Button('Sim', button_color=('white', 'green'), font=('Helvetica', 10), size=(10, 1), border_width=2, key='-SIM-'),
                 sg.Button('Não', button_color=('white', 'red'), font=('Helvetica', 10), size=(10, 1), border_width=2, key='-NAO-')],
                [sg.Text('', size=(10, 1), key='-RESULTADO-', justification='center', font=('Helvetica', 15),
                         text_color='white')]],
                justification='center')
            ]
        ]

    def inicio(self):
        
        # Criar janela
        self.janela = sg.Window('Simulador de dados', layout=self.layout,  size=(400, 200))

        while True:
            
            # Ler os valores da janela
            event, values = self.janela.Read()

            try:
                if event == sg.WIN_CLOSED or event == '-NAO-':
                    print('Agradecemos a sua participação!')
                    break
                elif event == '-SIM-':
                    self.valorDado()
            except Exception as e:
                print(f'Ocorreu um erro ao receber sua resposta: {e}')

        self.janela.close()

    def valorDado(self):
        resultado = random.randint(self.valor_minimo, self.valor_maximo)
        self.janela['-RESULTADO-'].update(f'Resultado: {resultado}')


simulador = SimuladorDado()
simulador.inicio()
