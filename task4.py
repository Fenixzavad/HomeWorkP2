# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n=int(input('Введите  N: '))
list_num=[ i for i in   range(-n,n+1)]
print(list_num)

file = open("file.txt","r")
a = file.readlines()
print(a)
for i in range(len(a)):
    a[i]=int(a[i].strip())
print(a)

product=0
for i in range(len(a)):
    product *=list_num[a[i]]
print(product)                