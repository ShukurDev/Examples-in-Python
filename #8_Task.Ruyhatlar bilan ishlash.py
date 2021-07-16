#1-T  O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ["O'zbekiston","Amerika","Koreya","Xitoy"]
print(davlatlar)

# 2-T Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))

# 3-T sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring

print(sorted(davlatlar))

# 4-T sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar,reverse = True))

#5-T sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.

davlatlar.sort()
print(davlatlar)

#6-T 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing

sonlar=list(range(120,1200,2))
print(sum(sonlar))
print(len(sonlar))
# 7-T Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(sonlar[:20])
print(sonlar[180:200])
print(sonlar[520:])

