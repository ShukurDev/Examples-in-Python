#(1) --> Web sahifangiz uchun foydalanuvchi (user) klassini tuzing.
# Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting
# (ism, foydalanuvchi ismi, email, va hokazo) (2) --> Klassga bir nechta metodlar qo'shing,
# jumladan get_info() metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin (masalan:
# "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).(3) --> Klassdan bir nechta obyektlar yarating
# va uning xususiyatlari va metodlariga murojat qiling.

class foydalanuvchi:
    def __init__(self,ism,familiya,email,login,tyil,tjoy,tnom):
        self.name =ism
        self.familiya= familiya
        self.email=email
        self.login=login
        self.tyil=tyil
        self.tjoy=tjoy
        self.tnom=tnom
    def get_info(self):
      return f"Foyadalanuvchi ismi = {self.name}.title().\nFamiliyasi = {self.familiya}\nElektron pohta manzili : {self.email}\nLogin = {self.login}\nTug'ulgan yili = {self.tyil}\nTug'ulgan joy = {self.tjoy}\nTel nomeri = {self.tnom}"
ismr=input("Foydalanuvchining ismini kiriting: ")
fm=input("Foydalanuvchining familiyasini kiriting: ")
em=input("Foyalanuvchining e-manzilini kiriting: ")
lg=input("Foyalanuvhcining loginni kiriting: ")
ty=int(input("Foyalanuchining tug'ilgan yilini kiriting: "))
tj=input("Foydalanuchining tug'ilgan joyini kiting : ")
tn=(input("Foydallanuchining tel nomrini kiting: "))
user=foydalanuvchi(ismr,fm,em,lg,tn,ty,tj)
print(user.get_info())
print("Ikkinchi foydalanuvchining ma'lumotlarini kiritng!")
ismr1=input("Foydalanuvchining ismini kiriting: ")
fm1=input("Foydalanuvchining familiyasini kiriting: ")
em1=input("Foyalanuvchining e-manzilini kiriting: ")
lg1=input("Foyalanuvhcining loginni kiriting: ")
ty1=int(input("Foyalanuchining tug'ilgan yilini kiriting: "))
tj1=input("Foydalanuchining tug'ilgan joyini kiting : ")
tn1=(input("Foydallanuchining tel nomrini kiting: "))
object1=foydalanuvchi(ismr1,fm1,em1,lg1,tn1,ty1,tj1)
print(user.__dict__)