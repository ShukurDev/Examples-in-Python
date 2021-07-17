# 18-lesson 1-task . Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing.
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
buyurtmalar = []
buy = "Nimalar buyurtirasiz:"
print("Hurmatli mijoz buyurtmalar ruyhatini kiritishingiz mumkin!")
while True:

    mahsulot = input(buy)
    buyurtmalar.append(mahsulot)
    order = input("Yana biron narsa buyurtirasizmi(ha/yo\'q): ")
    if order == 'ha':
        continue
    else:
        break
print("Sizning buyurtmalar ruyhatingiz quyidagicha: ")
for buyr in buyurtmalar:
    print(buyr.upper())


# 18-lesson 2-task.e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
mahsulotlar = {}
print("Mahsulotlaringizni kiritishingiz mumkin.")

while True:
    product = input("Mahsulotingizni noomini kiriting --> ")
    narx = int(input("Mahsulotingizning narxini kiriting--> "))
    mahsulotlar[product] = narx
    javob = input("Yana mahsulot kiritasizmi(yes/no) : ")
    if javob == 'yes':
        continue
    else:
        break
for product, narx in mahsulotlar.items():
    print(f"{product.upper()}ning narxi {narx} so'm")

# 18-lesson 3-task.Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni
# e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin).
# Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
mahsulotlar = {}

print("Mahsulotlaringizni kiritishingiz mumkin.")

while True:

    product = input("Mahsulotingizni noomini kiriting --> ")
    narx = int(input("Mahsulotingizning narxini kiriting--> "))
    mahsulotlar[product] = narx
    javob = input("Yana mahsulot kiritasizmi(yes/no) : ")
    if javob == 'yes':
        continue
    else:
        break

buyurtmalar = []
buy = "Nimalar buyurtirasiz:"
print("Hurmatli mijoz buyurtmalar ruyhatini kiritishingiz mumkin!")
while True:

    mahsulot = input(buy)
    buyurtmalar.append(mahsulot)
    order = input("Yana biron narsa buyurtirasizmi(ha/yo\'q): ")
    if order == 'ha':
        continue
    else:
        break
# print("Sizning buyurtmalar ruyhatingiz quyidagicha: ")


for product, narx in mahsulotlar.items():
    for buyr in buyurtmalar:
        if buyr == product:
            print(f"{product.title()}ning narxi {narx}")
        else:
            break
            print("Bizda bunday mahsulot yuq!")