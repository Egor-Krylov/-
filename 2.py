import numpy as np

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

def combinations (n, k):
    result = 1
    for i in range(n-k + 1, n + 1):
        result *= i
    
    for i in range(1, k + 1):
        result /= i
    return round(result, 5)

def bernulli (n, k, p):
    return round(combinations (n, k) * (p**k) * ((1-p)**(n-k)), 5)

def puasson (m, lambd):
    return round(((lambd ** m) / factorial(m)) * (2.7182818284 **(-lambd)), 5)

print(f'ответ на задачу 1: {bernulli(100, 85, 0.8)}')
print(f'ответ на задачу 2: {puasson (0,  5000 * 0.0004)}')
print(f'ответ на задачу 3: {bernulli(144, 70, 0.5)}')

noBlack = round((combinations(7, 2) / combinations(10, 2))*(combinations(9, 2) / combinations(11, 2)), 5)
noWhite = round((combinations(3, 2) / combinations(10, 2))*(combinations(2, 2) / combinations(11, 2)), 5)
twoWhiteFromFirst2BlackFromSecond = round((combinations(7, 2) / combinations(10, 2))*(combinations(2, 2) / combinations(11, 2)), 5)
oneWhiteFromFirstOneWhiteFromSecond = round(((combinations(7, 1) * combinations(3, 1)) / combinations(10, 2)) * ((combinations(9, 1) * combinations(2, 1)) / combinations(11, 2)), 5)
twoBlackFromFirst2WhiteFromSecond = round((combinations(3, 2) / combinations(10, 2))*(combinations(9, 2) / combinations(11, 2)), 5)
print(f'ответ на задачу 4: а) {noBlack}')
print(f'\t\t   б) {round(twoWhiteFromFirst2BlackFromSecond + oneWhiteFromFirstOneWhiteFromSecond + twoBlackFromFirst2WhiteFromSecond, 5)}')
print(f'\t\t   в) {(1 - noWhite)}')
