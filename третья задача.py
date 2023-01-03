#Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.
def f(n):
    sum = 0
    list = {i:((1+1/i)**i) 
    for i in range(1,n+1)}
    for i in list:
        sum += list.get(i)
    print('sum =',round(sum,2))
    return {i:((1+1/i)**i) for i in range(1,n+1)}
n = int(input("Введите количество чисел в последовательности: "))
print(f(n))