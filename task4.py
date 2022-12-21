# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n=int(input('Введите  N: '))
list_num=[ i for i in   range(-n,n+1)]
print(list_num)

file = open("file.txt","r")
a = file.readlines()
print(a)
