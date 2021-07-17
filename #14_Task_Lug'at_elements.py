# 1-T Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni ' \
# for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.


atamalar = {
    'integer':'Butun son',
    'float':'O\'nli kasr son',
    'string':'Matnlarni ifodalayi',
    'if':'Agar deb tarjima qillinadi.Shart operatori',
    'else':'Aks holda.',
    'print':'Chop qluvchi funksiya',
    'input':'Qabul qiluvchi funksiya.',
    'for':'tsikl loop',
    'while':'sikl operatori'
}
for k,e in sorted(atamalar.items()):
    print(f"{k.title()} - {e.title()}")

# 2 - T Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan
# 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan
# taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating,
# aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

menu = {
    'osh':20000,
    'manti':6000,
    'barak':19000,
    'shurva':15000,
    'lag\'mon':24000,
    'shashlik':8000,
    'somsa':5000,
    'non':3000
}
print("3 ta ovqat buyurtma bering:")
buyurtma= []
for i in range(3):
    buyurtma.append(input())
for b in buyurtma:
    if b in menu.keys():
        print(f"{b}-{menu[b]} so'm")
    else:
        print(f"Kechirasiz bizda {b} yo'q")










