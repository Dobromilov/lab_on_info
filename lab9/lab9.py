#1

# from functools import lru_cache
# @lru_cache(None)
#
# def func(x):
#     return x ** 2 / (10 + x ** 3)
#
# a = -2
# b = 5
# n = 100
# h = (b - a) / n
#
# f = [func(a + i * h) for i in range(n + 1)]
#
# integral = h / 2 * (f[0] + f[-1]) + h * sum(f[1:-1])
#
# print(integral)

#2
# from random import randint
#
# def f(a):
#     if a[0][2]+a[1][2]+a[2][2]==a[0][1]+a[1][1]+a[2][1]==a[0][0]+a[1][0]+a[2][0]==a[0][0]+a[1][1]+a[2][2]== \
#         a[0][2]+a[1][1]+a[2][0]==15:
#         return True
#     else:
#         return False
#
# x=1
# while x==1:
#     s = set()
#     matrix = [[randint(1, 9) for i in range(1, 4)] for j in range(1, 4)]
#     for i in range(0,3):
#       for j in range(0,3):
#             s.add(matrix[i][j])
#     if len(s)==9 and f(matrix)==True:
#         for el in matrix:
#             print(*el)
#         x=0

#3
 # def distance(a,b):
 #     arr=[]
 #     for i in range(n):
 #         arr.append(((b[0][0] - a[i][0])  2 + (b[0][1] - a[i][1])  2)**0.5)
 #     for i in range(n):
 #         if arr[i] == min(arr):
 #             return a[i]
 # n=int(input("Введите количество сокровищ: "))
 # a,b=[[0]*2 for i in range(n)],[[0]*2]
 # for i in range(n):
 #     for j in range(2):
 #         a[i][j] = int(input(f"Введите координату сокровища с позицией {i,j}: "))
 # b[0][0],b[0][1] = int(input("Введите координату Сани с позицией (0,0): ")),int(input("Введите координату Сани с позицией (0,0): "))
 # print(distance(a,b))

#4
# menu = [["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
#  ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
#  ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]]
#
# print("Меню: ")
# for x in range (3):
#     mas=menu[x][1]
#     print(f"{menu[x][0]}; Цена: {menu[x][2]}; Ингредиенты:",*mas)
# print()
#
# name=input("Блюдо которое вы ищите: ")
# for x in range(2):
#     mas = menu[x][1]
#     if name==menu[x][0]:
#         print(f"Цена: {menu[x][2]}; Ингредиенты:",*mas)
# print()
#
# menu.append([input("Новое блюдо: "),[input("Ингредиенты: ")],input("Цена: ")])
# print()
#
# for x in range (len(menu)):
#     menu[x][2]=input(f"Изменить цену у товара {menu[x][0]}: ")

#5
# from random import randint
# m=int(input())
# n=int(input())
# matrix = [[randint(0, 9) for i in range(1, n+1)] for j in range(1, m+1)]
#
# for el in matrix:
#     print(*el)
#
# matrix_new = [([0] * m) for _ in range(n)]
#
# for i in range(m):
#     for j in range(n):
#         matrix_new[j][i] = matrix[i][j]
# print()
#
# for el in matrix_new:
#     print(*el)

#6
# from random import randint
# n=int(input())
# matrix = [[randint(0, 9) for i in range(1, n+1)] for j in range(1, n+1)]
#
# for el in matrix:
#     print(*el)
# print()
#
# matrix_new=matrix
#
# start=0
# end=n-1
# for y in range(n):
#     matrix_new[start][y] = matrix[end][y]
#     matrix_new[end][y] = matrix[start][y]
#     start+=1
#     end-=1
#
#
# for el in matrix_new:
#     print(*el)
# print()

#7
# from random import randint
# m,n=int(input()),int(input())
# matrix = [[randint(0, 1) for i in range(0, n)] for j in range(1, m+1)]
#
# for el in matrix:
#     print(*el)
# print()
#
#
# count_hum=int(input())
# mx=0
# r=0
#
# for x in matrix:
#     count = 1
#     r+=1
#     for i in range(len(x)-1):
#         if x[i]==0 and x[i+1]==0:
#             count+=1
#         else:
#             mx=max(mx,count)
#             count=0
#     if count_hum<=mx:
#         print(r)
#         exit()

#8
# m, n = int(input()), int(input())
# matrix = [[0] * m for _ in range(n)]
#
# for i in range(m):
#     matrix[0][i] = 1
# for j in range(n):
#     matrix[j][0] = 1
#
# for i in range(1,n):
#     for j in range(1,m):
#         matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]
#
# print()
# for row in matrix:
#     print(*row)

#9
# from random import randint
# def f(matr):
#     count=0
#     for x in range(4):
#         for y in range(4):
#             if matr[x][y]==1:
#                 count+=1
#     if count==4:
#         return True
#     else:
#         return False
#
# while True:
#     matrix = [[randint(0, 1) for i in range(0, 4)] for j in range(0, 4)]
#     if f(matrix)==True:
#         break
#
# for row in matrix:
#     print(*row)
#
# count=0
# while True:
#     sms=input().split(" ")
#     if matrix[int(sms[1])-1][int(sms[0])-1]==1:
#         print("Вы попали!")
#         count+=1
#         if count == 4:
#             print("Молодец, ты выиграл!")
#             break
#     else:
#         print("Мимо. Попробуй еще!")
