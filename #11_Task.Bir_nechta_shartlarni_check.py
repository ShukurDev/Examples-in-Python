# 1-2-T mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
#  Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang.
#  Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring
#  va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda,
#  "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

mahsulot = ["anor","olma","behi","nok","xurmo","sabzi","shaftoli"]
n=int(input("Savatga Nechta mahsulot kiritasiz: "))
savat = []
dukonda_bor = []
dukonda_yuq = []
for i in range(n):
    savat.append(input(f"Savatga {i+1}-mahsulotingizni qushing: "))


for m in savat:
    if m in mahsulot:
        dukonda_bor.append(m)
        #print(f"Do'konmizda {m} bor.")
    else:
        dukonda_yuq.append(m)
        # print(f"Do'konimizda {m} yo'q.")

if dukonda_yuq:
    print("Quyidagi mahsulotlar dukonimizda yuq: ")
    for j in dukonda_yuq:
        print(j)
else:
    print("Siz soragan barcha mahsulotlar Do'konimizda bor!")

