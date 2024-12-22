# 1
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            elif arr[j][1] == arr[j+1][1]:
                if arr[j][2] > arr[j+1][2]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

count = int(input())
array = []

for i in range(count):
    name, status = input().split()
    if status == 'woman' or status == 'child':
        priority = 1
    elif status == 'man':
        priority = 2
    elif status == 'captain':
        priority = 3
    array.append([name, priority, i])
bubble_sort(array)
for person in array:
    print(person[0])


#2
# word = input().strip()
# if word[0]=='Q' and (word.count('Q')==word.count('A')) and word[-1:]!='Q':
#    print('+')
# else:
#    print('-')


#3
# import PySimpleGUI as sg
# import random
# c_image = [[sg.Image("bio.png")]]
# c_input = [[sg.Text("Введите количество бактерий:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="micro")],
#            [sg.Text("Количество секунд:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="count")],
#            [sg.Text("Результат:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(5, 0), key="res")],
#            [sg.Button("Рассчитать", font="Arial 20")]]
#
# layout = [
#     [sg.Column(c_image), sg.VSeperator(), sg.Column(c_input, justification='right')]
# ]
#
# window = sg.Window("Калькулятор бактерий", layout)
#
# while 1:
#
#     event, value = window.read()
#
#     if event == sg.WIN_CLOSED:
#         break
#
#     try:
#         micro = int(value["micro"])  # начальное количество бактерий
#         count = int(value["count"])  # количество секунд
#         k = 2  # коэффициент деления
#         res = micro
#
#
#         for _ in range(count):
#             b = random.randint(0, 4)
#             res = k * res + b  # обновление количества бактерий
#         window["res"].update(res)
#     except ValueError:
#         sg.popup_error("Введите корректные числовые значения!")
#
#
# window.close()

# #4
# import PySimpleGUI as sg
#
# layout = [
#     [sg.Text("Введите значение (от -128 до 127):")],
#     [sg.InputText(key='-INPUT-')],
#     [sg.Button("Решить"), sg.Button("Закрыть")],
#     [sg.Text("", size=(30, 1), key='-OUTPUT1-')],
#     [sg.Text("", size=(30, 1), key='-OUTPUT2-')],
#     [sg.Text("", size=(30, 1), key='-OUTPUT3-')]
# ]
#
# window = sg.Window("Окно", layout)
#
# while True:
#     event, values = window.read()
#     if event == 'Закрыть' or event == sg.WINDOW_CLOSED:
#         break
#     if event == "Решить":
#         user_input = values['-INPUT-']
#         try:
#             number = int(user_input)
#             if -128 <= number <= 127:
#                 if number >= 0:
#                     direct_code = bin(number)[2:].zfill(8)
#                 else:
#                     direct_code = bin(number & 0xFF)[2:].zfill(8)
#
#                 window['-OUTPUT1-'].update(f"Прямой код: {direct_code}", text_color='white')
#
#
#
#                 if number >= 0:
#                     reverse_code = direct_code
#                 else:
#                     reverse_code = direct_code[0] + direct_code[1:].replace('0', '*').replace('1', '0').replace('*', '1')  # Инвертируем биты, оставляем знак
#                 window['-OUTPUT2-'].update(f"Обратный код: {reverse_code}", text_color='white')
#
#
#
#                 if number >= 0:
#                     complement_code = direct_code
#                 else:
#                     complement_code = reverse_code[0] + reverse_code[1:].replace('0', '*').replace('1', '0').replace('*', '1')  # Инвертируем
#                     # Прибавляем 1
#                     complement_code_bin = bin(int(complement_code, 2) + 1)[2:].zfill(8)
#                     complement_code = complement_code_bin
#                 window['-OUTPUT3-'].update(f"Дополнительный код: {complement_code}", text_color='white')
#             else:
#                 window['-OUTPUT1-'].update("Ошибка: число вне диапазона!", text_color='red')
#                 window['-OUTPUT2-'].update("")
#                 window['-OUTPUT3-'].update("")
#         except ValueError:
#             window['-OUTPUT1-'].update("Ошибка: введите число!", text_color='red')
#             window['-OUTPUT2-'].update("")
#             window['-OUTPUT3-'].update("")
# window.close()
