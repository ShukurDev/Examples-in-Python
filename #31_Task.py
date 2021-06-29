# Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar qo'shing  
# va ularning qiymatini ko'rsatuvchi va o'zgartiruvchi metodlar yozing.
# from uuid import uuid4
class Shahs:
    """Asosiy klass!"""
    __odamlar_soni=0
    def __init__(self,ism,faml,teln,adres,yosh=10):
        self.ism=ism
        self.fm=faml
        self.__id=43564535
        self.teln=teln
        self.adres=adres
        self.__yosh=yosh
        Shahs.__odamlar_soni+=1
    
    #def get_info(self):
     #   return f"Salom {self.fm} {self.ism}\nTel nomeringizni  : {self.teln}\nAdress : {self.adres}\n"
    def get_id(self):
        j=self.__id*10
        return j
    def get_yosh(self,yil):

        return 2021-yil
    @classmethod
    def get_odam_s(cls):
        return f"Bu tadbirda  qatnashgan odamlar soni = ",cls.__odamlar_soni
  
class Talaba():
    __talabalar_soni=0
    def __init__(self,pcr,guruh,baho):
      #  super.__init__(self,pcr,guruh,baho)
        self.pcr=pcr
        self.guruh=guruh
        self.baho=baho
        self.__kontrakt=6400000
        self.__kism = "Ergash Domla"
        Talaba.__talabalar_soni+=1
    @classmethod
    def get_talabalar_soni(cls):
        return f"Bu musobaqada qatnashgan talabalar soni  =   ",cls.__talabalar_soni

    def get_kont(self,universitet):
        if universitet=='TATU UF':
            return self.__kontrakt+300000
        else:
            return self.__kontrakt
    def get_kism(self,guruh):
        if guruh>940:
            return self.__kism
        else:
            return 'Komil'
#  Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing 


    #def get_talab(cls):
    #    return cls.talabalar_soni

odam1=Talaba("Shukurali","Rezamonov",937990702)
odam2=Talaba("Shukurali","Rezamonov",937990702)
odam3=Talaba("Shukurali","Rezamonov",937990702)

odam4=Shahs("Shukurali","Rezamonov",937990702,"Suxondaryo viloyati",20)
odam5=Shahs("Shukurali","Rezamonov",937990702,"Suxondaryo viloyati",20)
odam6=Shahs("Shukurali","Rezamonov",937990702,"Suxondaryo viloyati",20)

print("1 - shahsning ID raqami: ",odam4.get_id())
print("Bu shahsning yoshi esa = ",odam4.get_yosh(2002))

print("2 - shahsning ID raqami: ",odam5.get_id())
print("Bu shahsning yoshi esa = ",odam5.get_yosh(2002))

print("Ularning soni = ",Shahs.get_odam_s())


print("Ruyhatdagi Talabalar soni = ",Talaba.get_talabalar_soni())
print("Ularning kontrakt summasi = ",odam1.get_kont("TATU UF)"))

print("1 - talabaning Kuratorining ismi : ",odam1.get_kism(941))

print("2 - talabaning Kuratorining ismi : ",odam2.get_kism(951))
print("3 - talabaning Kuratorining ismi : ",odam3.get_kism(931))


print(Shahs.get_odam_s())




