#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input('Введите число: '))
i = 0
n = 0
for j in range(number):
    if n <= number:
        n = pow(2, i)
        i +=1
        if n <= number:
            print(n, end = ' ')
            