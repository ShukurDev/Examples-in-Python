# 1- T Kamida 5 elementdan iborat ismlar degan 
# ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# ismlar = ["Aziz","Anvar","Ulug'bek","Sanajar","Sardor"]
# i=0
# for send in ismlar:
#     print(f"Assalomu alaykum {send} qandaysiz.")
#     i=i+1
# print(f"Kod {i} marta takrorlandi.")

# 2-T 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing.
#  Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
# toq =list(range(11,100,2))
# for i in toq:
#     print(i**3)


# 3-T Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang,
#  va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
# print("Foydalanuvchi eng sevimlli 5 ta kiningizni kiriting.")
# kinolar = []
# for i in range(5):
#     kinolar.append(input(f"{i+1} - sevmli konoingizni kiriting: "))
# print(kinolar)


# 4-T Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har
#  bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
son=int(input("Bugun nechta odam bilan uchrashdingiz:  "))
ruyhat = []
for i in range(son):
    ruyhat.append(input(f"Bugun {i+1}- uchrashgan oodamingizning ismi nima edi : "))
print(ruyhat)
