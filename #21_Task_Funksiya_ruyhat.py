
# 1-TASK. Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi
# harfini katta harfga o'zgatiruvchi funksiya yozing.
def katta_harf(ismlar):
    names = []
    for i in range(len(ismlar)):
        ismlar[i] = ismlar[i].title()
ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)



# 2-TASK.Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring
def katta_harf(ismlar):
    names = []
    while ismlar:
        ism = ismlar.pop()
        names.append(ism.title())
    return names
ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar[:])
print(ismlar)
print(yangi_ismlar)

