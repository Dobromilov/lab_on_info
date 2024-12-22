# student = {'user': 'Ivan', 'age': 12}
# print(student['user'])


#1
# dictionary={
#     '.':'1',
#     ',':'11',
#     '?':'111',
#     '!':'1111',
#     ':':'11111',
#     'A':'2',
#     'B':'22',
#     'C':'222',
#     'D': '3',
#     'E': '33',
#     'F': '333',
#     'G': '4',
#     'H': '44',
#     'I': '444',
#     'J': '5',
#     'K': '55',
#     'L': '555',
#     'M': '6',
#     'N': '66',
#     'O': '666',
#     'P': '7',
#     'Q': '77',
#     'R': '777',
#     'S': '7777',
#     'T': '8',
#     'U': '88',
#     'V': '888',
#     'W': '9',
#     'X': '99',
#     'Y': '999',
#     'Z': '9999',
#     '0': '0',
#     ' ': '0'
# }
#
# def f(text):
#     text=text.upper()
#     result=[]
#     for char in text:
#         if char in dictionary:
#             result.append(dictionary[char])
#     return ''.join(result)
#
# text=input()
# print(f(text))
#
#Кортежи
#2
# letter_scores = {
#     ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'): 1,
#     ('D', 'G'): 2,
#     ('B', 'C', 'M', 'P'): 3,
#     ('F', 'H', 'V', 'W', 'Y'): 4,
#     ('K',): 5,
#     ('J', 'X'): 8,
#     ('Q', 'Z'): 10
# }
#
# def f(text):
#     text=text.upper()
#     sum_result=0
#     for char in text:
#         for keys, value in letter_scores.items():
#             if char in keys:
#                 sum_result+=value
#                 break
#     return sum_result
#
# text=input()
# print(f(text))

#3
# emails = {
#     'gryffindor.com': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'k_stepanov'],
#     'hufflepuff.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
#     'hogwarts.com': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
#     'slytherin.com': ['ekaterina_ivanova', 'glebova_nastya'],
#     'ravenclaw.com': ['john.doe', 'mark.zuckerberg', 'helen_hunt']
# }
#
# for keys, word in emails.items():
#     if keys:
#         for result in word:
#             print(result+f'@{keys}')

# #4
import random
import PySimpleGUI as sg
# Определяем макет интерфейса
layout = [
    [sg.Image('file.png', key='-IMAGE-')],
    [sg.Text('Введите границы диапазона')],
    [sg.Text('Минимум:', size=(10, 1)), sg.Input(key='-MIN-', size=(15, 1))],
    [sg.Text('Максимум:', size=(10, 1)), sg.Input(key='-MAX-', size=(15, 1))],
    [sg.Button('Сгенерировать', size=(15, 1))],
    [sg.Text('Случайное число:', size=(15, 1)), sg.Input(key='-OUTPUT-', size=(15, 1), disabled=True)],  # Поле вывода
]

window = sg.Window('Рандом', layout)
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    if event == 'Сгенерировать':
        try:
            min_val = int(values['-MIN-'])
            max_val = int(values['-MAX-'])
            if min_val > max_val:
                sg.popup('Ошибка!', 'Минимальное значение больше максимального.')
            else:
                random_number = random.randint(min_val, max_val)
                window['-OUTPUT-'].update(random_number)
        except ValueError:
            sg.popup('Ошибка!', 'Введите корректные целые числа!')
window.close()

#5
# import PySimpleGUI as sg
# text_size = 17
# layout = [[sg.Text("Добро пожаловать в игру \"Эрудит\" Вводи свое слово! ",font=("Arial", text_size)),sg.InputText(key="word",font=("Arial", text_size),size=(20,2))],
#
#           [sg.Image(filename="file.png")],
#           [sg.Button("Посчитать сумму очков",font=("Arial", text_size),size=(20,1))],
#           [sg.Text("Сумма очков равна:",font=("Arial", text_size)),(sg.Text("",font=("Arial", text_size), key="Output"))]]
# window = sg.Window("game", layout,size=(1000,700))
# while 1:
#      event, values = window.read()
#      score = {'1': "AEILNORSTU", '2': 'DG', '3': 'BCMP', '4': 'FHVWY', '5': 'K', '8': 'JX', '10': 'QZ'}
#      string = str(values["word"]).upper()
#      final_score = 0
#      for symbol in string:
#           for points in score:
#                if symbol in score[points]:
#                     final_score += int(points)
#      if event == "Посчитать сумму очков":
#           window["Output"].update(final_score)
#      elif event == sg.WINDOW_CLOSED:
#           break
# window.close()
