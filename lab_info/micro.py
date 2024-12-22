import matplotlib.pyplot as plt
import math as m

# Определяем функцию для расчета U(t)
def func1(x):
    return 2.5 * m.exp(-b * x) * m.cos(w * x)

# Задаем параметры
w = 1666.67  # Частота затухающих колебаний
b = 20       # Коэффициент затухания

# Создаем списки для хранения значений x и y
x = []
y = []

# Генерируем значения для x и y
i = 0
while i <= 0.05:  # Удвоенное время релаксации (2*tau = 0.05 с)
    x.append(i)
    y.append(func1(i))
    i += 0.00001  # Шаг по времени

# Строим график
plt.plot(x, y)
plt.xlabel('Время, с')
plt.ylabel('Напряжение, В')
plt.title('Затухающие колебания напряжения на конденсаторе')
plt.grid(True)
plt.show()