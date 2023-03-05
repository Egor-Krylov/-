import numpy as np
from scipy import stats

print ('Задача 1:')
A1 = np.array([380,420, 290])
B1 = np.array([140,360,200,900])
test1 = stats.mannwhitneyu(A1, B1)
print(test1)
# MannwhitneyuResult(statistic=8.0, pvalue=0.6285714285714286)
print (f'pvalue>0.05 => Статистичестки значимых различий не выявлено\n')

print ('Задача 2:')

A2 = np.array([150, 160, 165, 145, 155])
B2 = np.array([140, 155, 150,  130, 135])
C2 = np.array([130, 130, 120, 130, 125])
test2 = stats.friedmanchisquare(A2, B2, C2)
print(test2)
# FriedmanchisquareResult(statistic=9.578947368421062, pvalue=0.00831683351100441)

print (f'pvalue<0.05 => Статистичестки значимые различия выявлены\n')

print ('Задача 3:')

test3 = stats.wilcoxon(A2, B2)

print(test3)
# WilcoxonResult(statistic=0.0, pvalue=0.0625)
print (f'pvalue>0.05 => Статистичестки значимых различий не выявлено\n')

print ('Задача 4:')

A4 = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
B4 = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
C4 = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])

test4 = stats.kruskal(A2, B2, C2)
print(test4)
# KruskalResult(statistic=10.213868613138692, pvalue=0.006054616097364561)
print (f'pvalue<0.05 => Статистичестки значимые различия выявлены\n')


print ('Задача 5:')


A5 = np.array([2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34])

sigma = np.std(A5, ddof=1)
mean = np.mean(A5)
t = (mean - 2.5)/(sigma/np.sqrt(len(A5)))

print(t)
print (f'табличное значение для альфа = 0.025 = 2.228 > t => Статистичестки значимых различий не выявлено\n')