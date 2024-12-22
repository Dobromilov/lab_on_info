import PySimpleGUI as sg
from random import choice
import os


# Проверяем, все ли нужные изображения доступны
required_images = ["22.png", "33.png", "11.png", "win.png", "fail.png", "draw.png"]
for img_name in required_images:
    if not os.path.exists(img_name):
        sg.popup_error(f"Ошибка! Файл {img_name} отсутствует в папке со скриптом.")
        exit(1)

# Установка темы и начальные настройки
text_size = 18  # Увеличенный размер шрифта
bot, human, count = 0, 0, 0  # Счет бота, игрока и количество сыгранных раундов
image = ["22.png", "33.png", "11.png"]  # Новые пути к изображениям

# Функция для обновления счета в окне игры
def score_updater():
    window["user_score"].update(human)  # Обновляем счет игрока
    window["bot_score"].update(bot)  # Обновляем счет бота

# Макет для выбора имени и количества раундов
layout2 = [
    [sg.Text("Введите имя", font=("Arial", text_size)),
     sg.Input(key="name_of_user", size=(300, 100), font=("Arial", text_size))],
    [sg.Text("Введите количество раундов", font=("Arial", text_size)),
     sg.Input(key="count_matches", size=(300, 100), font=("Arial", text_size))],
    [sg.Button("Начать игру", font=("Arial", text_size))]
]

choice_bot = sg.Window("Выбор параметров игры", layout2, size=(600, 300))  # Увеличенное окно выбора

while True:
    choice_of, values_of = choice_bot.read()  # Чтение событий и значений из окна
    if choice_of == "Начать игру" or choice_of == sg.WINDOW_CLOSED:
        if values_of["count_matches"] == "" or not values_of["count_matches"].isdigit():  # Проверка ввода количества раундов
            sg.popup("Введите количество раундов", font=("Arial", text_size))  # Предупреждение
        elif values_of["name_of_user"] == "" or values_of["name_of_user"].isdigit():  # Проверка имени игрока
            sg.popup("Ну имя то введи", font=("Arial", text_size))  # Предупреждение
        else:
            choice_bot.close()  # Закрываем окно выбора
            break

# Макет для основного игрового окна
layout = [
    [sg.Text("Камень, ножницы и бумага", font=("Arial", text_size), justification="center", size=(40, 1))],
    [sg.Text("Ваш ход, счет: ", font=("Arial", text_size)),
     sg.Text(human, key="user_score", font=("Arial", text_size)),
     sg.Text("Ход противника, счет: ", font=("Arial", text_size), size=(40, 1), justification="right"),
     sg.Text(bot, key="bot_score", font=("Arial", text_size))],
    [sg.Image(filename="static.png", key="user_choice", size=(450, 450)),  # Default placeholder
     sg.Image(filename="static.png", key="bot_choice", size=(450, 450))],
    [sg.Button("Камень", font=("Arial", text_size), size=(15, 1)),
     sg.Button("Ножницы", font=("Arial", text_size), size=(15, 1)),
     sg.Button("Бумага", font=("Arial", text_size), size=(15, 1))]
]

window = sg.Window('Игра', layout, size=(1000, 700))  # Увеличенное окно игры

while True:
    event, values = window.read()  # Чтение событий и значений
    if event == sg.WINDOW_CLOSED:
        break

    bot_move = choice(image)  # Случайный ход бота

    if event == "Камень":
        count += 1
        window["user_choice"].update(filename="22.png")
        window["bot_choice"].update(filename=bot_move)
        if bot_move == "33.png":
            bot += 1
        elif bot_move == "11.png":
            human += 1
        score_updater()

    elif event == "Бумага":
        count += 1
        window["user_choice"].update(filename="33.png")
        window["bot_choice"].update(filename=bot_move)
        if bot_move == "11.png":
            bot += 1
        elif bot_move == "22.png":
            human += 1
        score_updater()

    elif event == "Ножницы":
        count += 1
        window["user_choice"].update(filename="11.png")
        window["bot_choice"].update(filename=bot_move)
        if bot_move == "22.png":
            bot += 1
        elif bot_move == "33.png":
            human += 1
        score_updater()

    if count == int(values_of["count_matches"]):
        window.close()
        layout3 = [
            [sg.Text(" ", font=("Arial", text_size), key="win_lose_noone", justification="center", size=(40, 1))],
            [sg.Image(key="win_lose_noone_image", size=(400, 400))]
        ]
        result_window = sg.Window("Результат игры", layout3, finalize=True, size=(400, 400))
        if bot > human:
            result_window["win_lose_noone"].update(f"Вы проиграли! Счет: {human}:{bot}")
            result_window["win_lose_noone_image"].update(filename="fail.png")
        elif bot < human:
            result_window["win_lose_noone"].update(f"Вы выиграли! Счет: {human}:{bot}")
            result_window["win_lose_noone_image"].update(filename="win.png")
        else:
            result_window["win_lose_noone"].update(f"Ничья! Счет: {human}:{bot}")
            result_window["win_lose_noone_image"].update(filename="draw.png")
        while True:
            event1, _ = result_window.read()
            if event1 == sg.WINDOW_CLOSED:
                result_window.close()
                break
        break

with open('game_data.txt', 'a', encoding='utf-8') as file:
    file.write(f"{values_of['name_of_user']} {human}:{bot}\n")
