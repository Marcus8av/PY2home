#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input("Введите число: "))
p = 1
a = [p:= p * i for i in range(1, n + 1)]
print(a)