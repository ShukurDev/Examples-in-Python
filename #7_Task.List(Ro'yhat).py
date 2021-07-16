# 1-T ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ["Anvar","Ulug'bek","Umid"]

# 2- T Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
print(f"Salom {ismlar[0]},bugun choyxona bormi.\n{ismlar[1]} bugun choyxonaga boramizmi?.\n{ismlar[2]} ishingdan chiqib menga tel qilgin.")

# 3-T sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
sonlar = [3,5,546,-563,33.3,1]
# tuplamning 3-index ga 777 soni yuklandi
sonlar[3]=777
print(sonlar)
# tuplamning  2-indexiga 571 element yuklandi.
sonlar.insert(2,571)
# tuplamdan 33.3 elementi uchirib tashlandi.
sonlar.remove(33.3)
print(sonlar)
#  tuplmaga 234324 elementi qushildi.
sonlar.append(234324)
# tuplamdan 4 -indexdagi eement uchirib tashlandi.
del sonlar[4]
print(sonlar)
# tuplamdan 3 elementi ug'irib olindi
son1=sonlar.pop(3)
print(son1)

# 7-T Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
mehmonlar =["kursdoshlar","qarindoshlar","Do'stlar"]
mehmonlar.remove("kursdoshlar")
print(mehmonlar)
friends=[]

kk=mehmonlar.pop(0)
friends.append(kk)
print(friends)