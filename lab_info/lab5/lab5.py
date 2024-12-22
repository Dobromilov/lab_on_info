
#1
#print(int(input("кол-во дней:"))*86400+int(input("кол-во часов:"))*3600+int(input("кол-во минут:"))*60)

#2
'''n=str(int(input("N = ")))
k=int(input("K = "))
print(n[-k:])'''

#3
'''variable=str(int(input("Трёхзначное число: ")))
if len(variable)==3:
    print("sum = ",sum(map(int,variable)))
else:
    print("error..")'''

#4
'''option=int(input("1 or 2: "))
if option==1:
    print("Win")
else:
    print("loss")'''

#5
'''a=int(input("Сторона a: "))
b=int(input("Сторона b: "))
c=int(input("Сторона c: "))
if a+b>c and b+c>a and c+a>b:
    if a!=b!=c:
        print("Разносторонний")
    elif a==b==c:
        print("Равносторонний")
    elif a==b or b==c or c==a:
        print("Равнобедренный")
else:
    print("error..")'''
#6
'''month=int(input("Название месяца: "))
if month=='Январь' or month=='Март' or month=='Май' or month=='Июль' or month=='Август' or \
        month == 'Октябрь' or month=='Декабрь':
    print('31')
elif month=='Апрель' or month=='Июнь' or month=='Сентябрь' or month=='Ноябрь':
    print('30')
else:
    print('error..')'''

#7
'''number=str(input())
alph='QWERTYUIOPASDFGHJKLZXCVBNM'
n='0123456789'
if len(number)!=6 and len(number)!=7:
    print("error..")
else:
    if len(number)==7:
        if number[0] in n and number[1] in n and number[2] in n \
                and number[3] in n and number[4] in alph and number[5] in alph and number[6] in alph:
            print("Новый формат")
        else:
            print("error..")
    if len(number)==6:
        if number[0] in alph and number[1] in alph and number[2] in alph \
                and number[3] in n and number[4] in n and number[5] in n:
            print("Старый формат")
        else:
            print("error..")'''


# st = input()
# print(int(st, 2))