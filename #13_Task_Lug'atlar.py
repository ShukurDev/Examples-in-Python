# 1-T otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida
#  kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo).
#  Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :
# onam = {
#     'ism':'Gullbahor',
#     'tyil':1968,
#     'tjoy':'Oltnsoy tumani,Aliboy Butayev mahallasi'
# }
# akam = {
#     'ism':'Sarvar',
#     'manzil':'Mirishkor qishlog\'i',
#     'tyi':1989
# }
# opam = {
#     'familiyasi':'Rezamonov',
#     'yoshi':2021-1991,
#     'ism':'Gulzoda'
# }
# print(f"Mening onamning ismi - {onam['ism']},Yoshi : {2021-onam['tyil']},{onam['tyil']}- yil,{onam['tjoy']} da tug'ilgan")
# print(f"Mening opamning ismi,familiyasi : {opam['familiyasi']} {opam['ism']},Yosh : {opam['yoshi']} da.")


# 2-T Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin
# . Kamida uch kishining sevimli taomini konsolga chiqaring: 
# taomlar = {
#     'Dadam':'Osh',
#     'Ayam':'yupqa',
#     'Akam':'Manti',
#     'opam':'Shurva',
#     'Men':'Quymoq'
#     }
# for i in taomlar:
#     print(f"{i.title()}ning sevimli taomi :{taomlar[i]}")


# 3-T Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting 
# (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.

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
n=input("Kalit so'zni kiriting : ")
# 1- usul
# print(atamalar.get(n,'Bunday so\'z mavjud emas'))

# 2-usul
#if n in atamalar:
#    print(atamalar[n])










