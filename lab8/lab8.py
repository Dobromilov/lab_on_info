#1
# string=input().split(" ")
# char=[]
# digits=[]
# for i in range(len(string)):
#     if string[i].isdigit():
#         char.append(string[i])
#     else:
#         digits.append(string[i])
# print(*char)
# print(*digits)

#2
# list=[[1, 2, ['Ok!', 3]], ['list', 4], 5]
# print(list[0][2][0])

#3
# array=input().split(" ")
# for i in range(len(array)-1):
#     if array[i]>array[i+1]:
#         print(array[i],end=' ')

#4
# def average(x,y):
#     return float(x/y)
#
# array=[]
# sum=0
# while True:
#     st=input()
#     if st=='':
#         break
#     else:
#         array.append(int(st))
#         sum += int(st)
# aver=average(sum,len(array))
# below_average = [num for num in array if num < aver]
# equal_to_average = [num for num in array if num == aver]
# above_average = [num for num in array if num > aver]
# print(aver)
# print(*below_average)
# print(*equal_to_average)
# print(*above_average)

#5
# array=input().split(" ")
# x=int(input())
# array.append(x)
# for i in range(len(array)):
#     array[i]=int(array[i])
# array=sorted(array)[::-1]
# ind=0
# for i in range(len(array)):
#     if array[i]==x:
#         ind=i
# print(ind+1)

#6
# import random
# array=[]
# i=0
# count=3
# while i!=3:
#     array+=random.choice(["О","Р"])
#     i+=1
# i=0
# while True:
#     array += random.choice(["О", "Р"])
#     count+=1
#     for i in range(len(array)-2):
#         if array[i] == array[i + 1] == array[i + 2]:
#             print(*array,count)
#             exit()

#7
# card=input()
# if len(card)!=16:
#     print("error..")
# else:
#     sum_c,sum_n=0,0
#     for i in range(len(card)):
#         if i%2==0:
#             sum_c+=int(card[i])
#         else:
#             if (int(card[i]) * 2)<=9:
#                 sum_n+=int(card[i])*2
#             else:
#                 sum_n+=int(card[i])*2-9
#     if (sum_c+sum_n)%10==0:
#         print("uncorrectly")
#     else:
#         print("correctly")

#8
# count,i=int(input()),0
# while i!=count:
#     s=input()
#     if len(s)>10:
#         print(s[0]+f"{len(s)-2}"+s[-1])
#     else:
#         print(s)
#     i+=1

#9
# n,count=int(input()),0
# while n!=0:
#     a=input().split()
#     if int(a[0])<int(a[1])-1:
#         count+=1
#     n-=1
# print(count)