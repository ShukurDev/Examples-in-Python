# 16 - Lesson.Practice 1-task Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni
# lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
ilmfan = {
    'ismi': 'Muhammad ibn muso  Al-Xorazmiy',
    'yili': 783,
    'manzil':'xiva',
    'umr':69
    }
sanat = {
    'ismi': 'Ozodbek Nazarbekov',
    'yili': 1970,
    'manzil':'Andijon viloyati',
    'umr': 60
    }
internet ={
'ismi': 'Bill Geyts',
    'yili': 1960,
    'manzil':'Amerika',
    'umr':70
    }
you=[ilmfan,sanat,internet]
for my in you:
    print(f"{my['ismi'].title()}"
          f"{my['yili']} - yilda"
          f"{my['manzil']} da tugilgan."
          f"{my['umr']} yil umr kurgan.\n")


# 16 - Lesson.Practice 2-tesk Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
# For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
shoir = {
  'abu Abdulloh' : ['as-sahih','al-mufrat','al kubrat'],
  'Abdulla Qahhor' : ['odob','ona','utgan tunlar'],
  'Erkin vohidov' : ['tong nafasi','ozbegim','qushlar'],
}
for ism,tillar in shoir.items():
  print(f"{ ism.title()}ning mashhur asarlaei")
  for til in tillar:
    print(til.upper())

# 16 -Lesson 4-task Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang.
# Har bir davlat haqida ma'lumotni konsolga chiqaring.
davlat = {
    'ozbekiston': {
        'poytaxt': 'Toshkent',
        'hududi': 448978,
        'aholisi': 33000000,
        'pul birligi': 'som'
    },
    'rossiya': {
        'poytaxt': 'moskva',
        'hududi': 1244344524,
        'aholisi': 245335353535,
        'pul birligi': 'rubl'
    },
    'aqsh': {
        'poytaxt': 'vashington',
        'hududi': 1436474234737,
        'aholisi': 3213123237123712,
        'pul birligi': 'dollar'
    }
}
for ism, info in davlat.items():
    print(f"{ism.title()}ning Poytaxti {info['poytaxt'].title()}\n"
          f"Hududi = {info['hududi']},\n"
          f"Aholisi = {info['aholisi']},\n"
          f"Pul birligi = {info['pul birligi']}")
