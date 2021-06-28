
#Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr
# sifatida uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])
#   1-Task
#class Talaba:
#    """ Talaba klassi"""
#    def __init__(self,ism,familiya,tyil,yjoy):
#        self.ism=ism
#        self.fliya=familiya
#        self.tyil=tyil
#        self.yjoy=yjoy
#        self.fanlar=[]
#    def get_ruyhat(self):
#        return f"{self.fanlar} !!!"

#talaba1=Talaba("Shukurali","Rezamonov",2002,"mirishkor")
#print(talaba1.get_ruyhat())


# 2-Task

# Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektl
#class Fan:
#    def __init__(self,fann,usoni,uqsoni,kitoblar_r,baholar):
#        self.fann=fann
#        self.usoni=usoni
#        self.uqsoni=uqsoni
#        self.kitoblar=kitoblar_r
#        self.baho=baholar
#        self.uquvchilar_i=[]
#        self.uquvchilar_f=[]
#    def get_fan1(self):
#       return f"{self.uquvchilar_f} {self.uquvchilar_i} {self.fann} - fani!\nBu fanni utadigan uqituvchilar soni : {self.uqsoni}\nFanga qatnashuvchi uquvchilar soni - {self.usoni}.\nKitoblar ruyhati: {self.kitoblar}.\nFan buyicha uquvchilarga quyilgan baholar : {self.baho}."
 

#t1=Fan("Fizika",26,4,"baddiy kitoblar",5)
#print(t1.get_fan1())



# 3-Task

# Talaba klassiga fanga_yozil() degan yangi metod yozing.
#  Bu metod parametr sifatida Fan klassiga tegishli
#  obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.
#class Fan:
#    def __init__(self,fann,usoni,uqsoni,kitoblar_r,baholar):
#        self.fann=fann
#        self.usoni=usoni
#        self.uqsoni=uqsoni
#        self.kitoblar=kitoblar_r
#        self.baho=baholar
#        self.uquvchilar_i=[]
#        self.uquvchilar_f=[]
#    def get_fan1(self):
#        return f"{self.uquvchilar_f} {self.uquvchilar_i} {self.fann} - fani!\nBu fanni utadigan uqituvchilar soni : {self.uqsoni}\nFanga qatnashuvchi uquvchilar soni - {self.usoni}.\nKitoblar ruyhati: {self.kitoblar}.\nFan buyicha uquvchilarga quyilgan baholar : {self.baho}."
#talaba1=Fan("adabiyot",34,12,"uqish",5)

#class Talaba:
#    """Tlaba klassning ruyhatiga fanlar qushiladi"""
#    def __init__(self,ism,flya,guruhi):
#        self.ism=ism
#        self.fml=flya
#        self.guruh=guruhi
#        self.fanlar=[]
#    def fanga_yozil(self,x):
#        self.fanlar.append(x)

#Talaba.fanga_yozil(talaba1)
#print(Talaba.fanga_yozil())


#  5-Task

# Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring 
# (masalan Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)
class Shahs:
    def __init__(self,ism,fmya,tyil,tjoy):
        self.ism=ism
        self.fmya=fmya
        self.tyil=tyil
        self.tjoy=tjoy
        self.nomzodlar=[]
    def get_info(self):
        return f"ismi - {self.ism}.\nFamiliyasi - {self.fmya}.\nTug'ilgan yili - {self.tyil}.\nTug'ilgan joy - {self.tjoy}."
    def get_name(self,nomzod):
        self.nomzodlar.append(nomzod)
        return self.nomzodlar
class Professor(Shahs):
    def __init__(self,ism,fmya,tyil,tjoy,ideraqam):
       super().__init__(ism,fmya,tyil,tjoy)
       self.id=ideraqam
       self.oyligi=50000
   
p1=Professor("Shukurali","Rezamonov",2002,"mirishkor",65546)
p1.get_name("Dasturchi")
p1.get_name("Quruvchi")
p1.get_name("Uqituvchi")
p1.get_name("Haydovchi")
p1.get_name("Uchuvchi")
p1.get_name("Yurist")
print(p1.get_info())
print(f"Foydalanuvchilar kaspi : ",p1.get_name("Novvoy"))
#class Foydalanuvchi(Shahs):
