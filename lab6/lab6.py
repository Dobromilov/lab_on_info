#1

# height=1
# mx=0
# mn=10**10
# while height!=0:
#     height=int(input())
#     if height!=0:
#         mn = min(height, mn)
#     else:
#         break
#     mx=max(mx,height)
# print(f"max:{mx}, min:{mn}")

#2

# sm=0
# for i in range(2,101):
#     if i%2==0:
#         sm+=i
# print(sm)

#3

# sm=0
# for i in range(1,int(input())+1):
#     sm+=i**2
# print(sm)

#4

# n = int(input("Введите высоту ёлочки: "))
# sim = "#"
# for i in range(1, n + 1):
#     for x in range(n - i):
#         print(" ", end="")
#     for y in range(2 * i - 1):
#         print(sim, end="")
#     print()
# print(' '*(n-1)+sim)

#5

# years_hum=int(input())
# years_dog=0
# if 0<years_hum<=2:
#     print(10.5*years_hum)
# if years_hum>2:
#     print(21+4*(years_hum-2))
# if years_hum<0:
#     print("error..")

#6

# import random
# a=0
# while a!=1:
#     secret = random.randint(1, 10)
#     print("Хорошо, я загадал число. Попробуй его отгадать")
#     count=1
#     while 1:
#         num = int(input("> "))
#         if num == secret:
#             print(f"{count}) Поздравляю! Вы угадали!")
#             break
#         else:
#             if num>secret:
#                 print(f"{count})Нее, ты не угадал. Попробуй снова. Secret меньше")
#                 count+=1
#             else:
#                 print(f"{count})Нее, ты не угадал. Попробуй снова. Secret больше")
#                 count+=1
#     s=input("Хотите сыграть снова? : ")
#     if s=="Да" or s=="да" or s=="yes" or s=="Yes":
#         a=0
#     else:
#         a=1

#7

# s=input()
# if len(s)==6:
#     if sum(map(int,(s[0]+s[1]+s[2])))==sum(map(int,(s[3]+s[4]+s[5]))):
#         print("Ваш билет счастливый")
#     else:
#         print("Обычный билет - туалетная бумага")
# else:
#     print("error..")

#8
# print(int(input(),2))

