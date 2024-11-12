#1
# file=open("file4.txt",encoding="UTF-8").readlines()
# mx=0
# for x in file:
#     text=x.split(" ")
#     mx=max(mx,int(text[2]))
# for x in file:
#     text=x.split(" ")
#     if mx==int(text[2]):
#         print(x)
# file.close()

#2
# for x in open('file5.txt',encoding="UTF-8").readlines():
#     text=x.split(" ")
#     for y in text:
#         if y=="Academy":
#             print("file5")
#             exit()
# for x in open('file6.txt',encoding="UTF-8").readlines():
#     text=x.split(" ")
#     for y in text:
#         if y=="Academy":
#             print("file6")
#             exit()

#3
# count=0
# count_e=0
# for x in open('file6.txt',encoding="UTF-8").readlines():
#     text=x.split(" ")
#     for y in text:
#         if y.count('E')>0 or y.count('e')>0:
#             count_e+=1
#         count+=1
# print(count_e/count*100)

#4
# name_man=open('file8.txt',encoding="UTF-8").readlines()
# name_girl=open('file7.txt',encoding="UTF-8").readlines()
# string=input()
# count=int(input())
# if string=='м' or string=='М':
#     for i in range(count):
#         print(name_man[i])
# else:
#     for i in range(count):
#         print(name_girl[i])
# name_man.close()
# name_girl.close()

#5
# file = open("file6.txt", "r",encoding="UTF-8")
# content = file.read().split(" ")
# count=int(len(content)/2)
# new_text=input()
# content[count]=content[count]+' '+new_text
# print(content[count])
# print(" ".join(content))
# file.close()

#6
# def f(x):
#     return x[::-1]
# file = open("file6.txt", "r",encoding="UTF-8")
# content = file.read().split(" ")
# content_new = []
# for x in content:
#     content_new.append(f(x))
# print(*content_new)
# file.close()

#7
# from random import randint
# file = open("file6.txt", "r",encoding="UTF-8")
# content = file.read().split(" ")
# the_first_part,the_second_part=randint(0, len(content)),randint(0, len(content))
# print(''.join(content[the_first_part]+content[the_second_part]))
# file.close()

#8
# n=int(input())
# m=int(input())
# k=0
# for i in range(n):
#     if i%2==0:
#         print("#"*m)
#         continue
#     if k==0:
#         print('.'*(m-1)+'#')
#         k+=1
#     else:
#         print('#'+'.' * (m - 1))
#         k=0
