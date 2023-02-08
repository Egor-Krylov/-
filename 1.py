import numpy as np

def combinations (n, m):
    result = 1
    for i in range(n-m + 1, n + 1):
        result *= i
    
    for i in range(1, m + 1):
        result /= i
    return result

print(f'ответ на задачу 1: а) {round(combinations(13,4)/combinations(52,4), 5)}  б) {round((combinations(4,1) * combinations(51,3))/combinations(52,4), 5)}')
print(f'ответ на задачу 2: {round(1 / combinations(10,3), 5)}')
print(f'ответ на задачу 3: {round(combinations(9,3)/combinations(15,3), 5)}')
print(f'ответ на задачу 4: {round(1/combinations(100,2), 5)}')
