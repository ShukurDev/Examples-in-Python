# exemple moules from python - modullarga misol pythondan
# 1-m
import math # Bu modul barcha matematik ammalllarni uz ichiga oladi.
print(math.sqrt(100))

# 2-m
from math import sqrt,pow # bunda esa math modulidan 2 ta sqrt va pow funksiyalari import qilinayapti
print(pow(2,3))

# 3-m
from math import*# bunda math modulidagi barcha funnksiyallarni import qiladi.tavfsiya qilinmaydi bu usul.
print(asin(10))

# 4-m
import random as r # bu moduldagi randit funksiyasi malum chegaradan tasodifiy raqamni tanllab qaytaradi.bu yerda r randomni qisqartmasi.
print(r.randit(1,10))

# 5-m choice(x) funksiyasi ham random modulidan
ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
print(ism)
print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz

# 6-m.  shuffle(x) x ichidagi elementlarni tasodifiy tartibda
# qaytaruvchi funksiya. Bunda x bir necha elementdan iborat o'zgaruvchi (matn, ro'yxat) bo'lishi kerak

x = list(range(11))
print(x)
r.shuffle(x)
print(x)

# Pythondagi moullar bilan tanishish uchun manzil:   https://docs.python.org/3/py-modindex.html#cap-l