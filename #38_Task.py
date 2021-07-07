#import datetime as dt

# sana = dt.datetime.now()
# print("Hozirgi vaqt!")
# print(sana.year)
# print(sana.month)
# print(sana.day)
# print(sana.hour)
# print(sana.minute)
# print(sana.second)
# print("Ertangi sana: ")
# sana1 = dt.datetime(2021,7,7,2,36)
# print(sana1)
# bugun = dt.date.today()
# print(bugun)
# farq= bugun.day
# print(farq)
# j=0
# while j!=10:
#     print(dt.date(2021,7,farq))
#     farq=farq+2
#     j=j+1

# 1- Task
# print(dt.date(2021,7,3))
# print(dt.date(2021,7,17))
# print(dt.date(2021,7,31))
# print(dt.date(2021,8,14))
# print(dt.date(2021,8,28))
# print(dt.date(2021,9,12))
# print(dt.date(2021,9,26))
# print(dt.date(2021,10,10))
# print(dt.date(2021,10,24))

# 2-Task
# bugun = dt.date.today()
# bugun1=bugun.day
# sana = dt.date(2021,7,20)
# qurbon_hayit = sana.day
# qolgan = bugun1 - qurbon_hayit

# print(f"Qurbon hayitiga {qolgan} kun qoldi")

# 3-Task

# hsana =dt.datetime.today()
# hyil = hsana.year
# tsana = dt.date(2002,7,14)
# ttyil=tsana.year
# def qayt(ts,ty):
#     yil = ts - ty
#     oy = yil * 12
#     kun = oy * 365
#     print( f"Tug'ilgan yilimdan hozirgacha:\n{yil} yil.\n{oy}  oy.\n{kun}  kun  tdi.")
# qayt(hyil,ttyil)

# 4-task

# import re

# raqam =str(input())
# suz ="Assalomualaykum"
# andoza = "As............m"
# andoza1="93.....02"
# print(re.match(andoza,suz))

# print(re.match(andoza1,raqam))

# 5 - Task

# import re 

# matn = """Assalom alaykum hurmatli do/'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI"
# matn2 = "Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test
# """

# andoza ="https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"

# print(re.findall(andoza,matn))

