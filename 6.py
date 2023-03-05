import numpy as np
from scipy import stats

print ('Задача 1:')

print (f'С вероятностью 95% истинное мат. ожидание лежит в интервале: [{80 - 1.96}, {80 + 1.96}]\n')

print ('Задача 2:')

array = np.array([6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1])
mean = array.mean()
std = array.std(ddof=1)
t1 = stats.t.ppf(0.975, 9)
print (f'С вероятностью 95% истинное значение лежит в интервале: [{round(mean - t1*(std/np.sqrt(10)), 2)}, {round(mean + t1*(std/np.sqrt(10)), 2)}]\n')

print ('Задача 3:')

mothers = np.array([175, 167, 154, 174, 178, 148, 160, 167, 169, 170])
daughters = np.array([178, 165, 165, 173, 168, 155, 160, 164, 178, 175])
delta = mothers.mean() - daughters.mean()
t2 = stats.t.ppf(0.975, 18)
D = (np.var(mothers, ddof=1) + np.var(daughters, ddof=1))/2
S = np.sqrt(D/5)
print (f'С вероятностью 95% истинная разность среднего роста родителей и детей лежит в интервале: [{round(delta - t2*S, 2)}, {round(delta + t2*S, 2)}]')