import numpy as np

list = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

def combinations (n, k):
    result = 1
    for i in range(n-k + 1, n + 1):
        result *= i
    
    for i in range(1, k + 1):
        result /= i
    return round(result, 5)

average = 0
for i in list:
    average += (i/(len(list)))

disp = 0

for i in list:
    disp += ((average - i)**2/(len(list) - 1))

dispShifted = 0
for i in list:
    dispShifted += ((average - i)**2/len(list))

sigma = np.sqrt(disp)

print ('Задача 1:')

print (f'Среднее арифметическое равно {round(average, 2)}')
print (f'Среднее квадратичное равно {round(sigma, 2)}')
print (f'Несмещенная дисперсия равна {round(disp, 2)}')
print (f'Смещенная дисперсия равна {round(dispShifted, 2)} \n')

print ('Задача 2:')

twoFromFirst = ((combinations(5, 2)/combinations(8, 2))*(combinations(5, 1)) * (combinations(7,3) / combinations(12, 4)))
oneFromFirst = (combinations(5, 1) * combinations(3, 1)/combinations(8, 2)) * (combinations(5, 2) * combinations(7,2) / combinations(12, 4))
zeroFromFirst = (combinations(3, 2)/combinations(8, 2)) * (combinations(5, 3) * combinations(7,1) / combinations(12, 4))
print (f'Ответ: {round(twoFromFirst + oneFromFirst + zeroFromFirst, 2)}\n')

print ('Задача 3:')

print (f'а: {round(0.9 * (1/3) / (0.9 * (1/3) + 0.8 * (1/3) + 0.6 * (1/3)), 2)}')
print (f'б: {round(0.8 * (1/3) / (0.9 * (1/3) + 0.8 * (1/3) + 0.6 * (1/3)), 2)}')
print (f'в: {round(0.6 * (1/3) / (0.9 * (1/3) + 0.8 * (1/3) + 0.6 * (1/3)), 2)}\n')

print ('Задача 4:')

print (f'а: {round(0.8 * 0.25 / (0.8 * 0.25 + 0.7 * 0.25 + 0.9 * 0.5), 2)}')
print (f'б: {round(0.7 * 0.25 / (0.8 * 0.25 + 0.7 * 0.25 + 0.9 * 0.5), 2)}')
print (f'в: {round(0.9 * 0.5  / (0.8 * 0.25 + 0.7 * 0.25 + 0.9 * 0.5), 2)}\n')

print ('Задача 5:')

print(f'а: {round(0.1 * 0.2 * 0.25, 4)}')
print(f'а: {round(0.1 * 0.2 * 0.75 + 0.9 * 0.2 * 0.25 + 0.1 * 0.8 * 0.25, 4)}')
print(f'а: {round(0.1 * 0.8 * 0.75 + 0.9 * 0.2 * 0.75 + 0.9 * 0.8 * 0.25, 4)}')
print(f'а: {round(1 - 0.9 * 0.8 * 0.75 - 0.1 * 0.2 * 0.25, 4)}')




