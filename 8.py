import numpy as np
from scipy import stats
import pandas

print ('Задача 1:')

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])

ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

zpks = np.array([zp[i]*ks[i] for i in range(len(ks))])

cov1 = round(np.mean(zpks) - np.mean(zp) * np.mean(ks), 2)
cov2 = np.cov(zp, ks, ddof=0)
print(f'ковариация вручную: {cov1}, ковариация фунцией: {cov2[1][0]}')
pirs1 = cov1 / (np.std(zp, ddof=0) * np.std(ks, ddof=0))
pirs2 = np.corrcoef(zp, ks)
zpp = pandas.Series(zp)
ksp = pandas.Series(ks)
pirs3 = zpp.corr(ksp)
print(f'коэффициент Пирсона вручную: {pirs1}, коэффициент Пирсона фунцией numpy: {pirs2[1][0]}, коэффициент Пирсона фунцией pandas: {pirs3}\n')

print ('Задача 2:')

iq = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])

t = stats.t.ppf(0.975, 9)
mean = np.mean(iq)
std = np.std(iq, ddof=1)
halfLen = t*std/np.sqrt(10)

print (f'С вероятностью 95% истинное мат. ожидание лежит в интервале: [{mean - halfLen}, {mean + halfLen}]\n')

print ('Задача 3:')

z = 1.96
mean2 = 174.2
std2 = 5
halfLen2 = z*std/np.sqrt(27)

print (f'С вероятностью 95% истинное мат. ожидание лежит в интервале: [{mean2 - halfLen2}, {mean2 + halfLen2}]\n')
