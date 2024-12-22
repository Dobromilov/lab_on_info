#1
# a="Довольно распространённая ошибка ошибка – это лишний повтор повтор слова слова . Смешно , не не правда ли ? Не нужно портить хор хоровод .".split(" ")
# mas=[]
# for i in range(0,len(a)-1):
#     if a[i]!=a[i+1]:
#         mas.append(a[i])
# mas.append(a[len(a)-1])
# for i in range(len(mas)):
#     print(mas[i], end=" ")

#2
# value=input("Введите два слова через пробел: ")
# value=value.split(" ")
# if len(value)!=2:
#     print("error...")
# else:
#     value=value[::-1]
#     for i in range(len(value)):
#         print(value[i],end=" ")

#3
# def f(x):
#     return '.'.join(x)
# print(f(input()))

#4
# st=input()
# if "не плохой" in st:
#     st=st.replace("не плохой","хороший")
# if "не плохая" in st:
#     st=st.replace("не плохая","хорошая")
# if "не плохо" in st:
#     st=st.replace("не плохо","хорошо")

#5
# st=input().split("/")
# if len(st)!=3:
#     print("Не хайку. Должно быть 3 строки.")
# else:
#     mas=[]
#     for i in range(len(st)):
#         sum=(st[i].count("а") + st[i].count("е") + st[i].count("и") + st[i].count("о") +
#         st[i].count("у") + st[i].count("ы") + st[i].count("э") + st[i].count("ю") +
#         st[i].count("я") + st[i].count("А") + st[i].count("Е") + st[i].count("И") +
#         st[i].count("О") + st[i].count("У") + st[i].count("Ы") + st[i].count("Э") +
#         st[i].count("Ю") + st[i].count("Я"))
#         mas.append(sum)
# if mas==[5,7,5]:
#     print("Хайку!")
# else:
#     print("Не хайку.")

#6

# st=input()
# if st[-1]!="#":
#     print("ты - ишак, неверно")
# else:
#     st=st[:-1]
#     s_new=''
#     while len(st)!=0:
#         s_new+=st[:1]
#         st=st[1:]
#         st=st[::-1]
#     print(s_new)
#хрень, т.к. неправильно понял условие и решил жопой наперед

# word,new_word,new_word_1=input(),"",""
# if word[-1]=="#":
#     word=word[:-1]
#     for i in range(len(word)):
#         if i % 2 == 0:
#             new_word+=word[i]
#         else:
#             new_word_1= word[i]+new_word_1
# else:
#     print("отсутствует знак #")
# print(new_word+new_word_1)

#7
# import random
#
# len_pas=int(input("желаемую длину пароля (целое число)"))
# up=input("нужны ли заглавные буквы (да/нет)")
# down=input("нужны ли строчные буквы (да/нет)")
# dig=input("нужны ли цифры (да/нет)")
# spec=input("нужны ли специальные символы (да/нет)")
#
# password=""
#
# alf_up='QWERTYUIOPASDFGHJKLZXCVBNM'
# alf_down='qwertyuiopasdfghjklzxcvbnm'
# alf_s=";:?,.<>`~[]{}|/-=+)(*&^%$#@!"
# alf_dig='0123456789'
# for i in range(len_pas):
#     if up=="да":
#         password += random.choice(alf_up)
#     if down=="да":
#         password += random.choice(alf_down)
#     if dig=="да":
#         password += random.choice(alf_dig)
#     if spec=="да":
#         password += random.choice(alf_s)
# if len(password) >= len_pas:
#         password=password[:len_pas]
#         print(password)


#8
# scoreboard=input()
# def f(a):
#     return a.split()
# def team(a):
#     return a.split("-")
# def score(a):
#     return a.split(":")
# teams=team(f(scoreboard)[0])
# scores=score(f(scoreboard)[1])
# if int(scores[0])>int(scores[1]):
#     print(teams[0])
# elif int(scores[0])<int(scores[1]):
#     print(teams[1])
# else:
#     print("Ничья")