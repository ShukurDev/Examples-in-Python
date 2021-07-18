# 1-Task.funksiya ikkita argument qabul qiladi  va aylana uzunligini qaytaradi:

import math
uzunlik = lambda a,b:2*math.pi*a*b
print(uzunlik(5,10))


# 2-Task
def daraja(n):
    return lambda x : x**n
kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")

# 3-Task. map() FUNKSIYASI
from math import sqrt

sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
ildizlar = list(map(sqrt,sonlar))

# exemple 2
kvadratlar = list(map(lambda x:x*x,sonlar))
print(kvadratlar)


# 4-Task. filter() FUNKSIYASI

import random as r

sonlar = r.sample(range(100),10) # 0-99 oralig'ida 10 ta tasodifiy sonlar

def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
    return x%2==0

juft_sonlar = list(filter(juftmi,sonlar))
print(sonlar)
print(juft_sonlar)

# exemple-3

mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda meva:meva.startswith('b'),mevalar))
print(mevalar_b)