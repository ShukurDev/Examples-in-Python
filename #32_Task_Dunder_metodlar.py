# 1 - Avvalga darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli  dunder metodlarni qo'shishni mashq qiling. 
# 2 - Obyekt haqida ma'lumot (__rerp__)
# 3 - Talabalarni bosqichi bo'yicha solishtirish (__lt__,__eg__ va hokazo)

class Shahs:
    """Asosiy klass!"""
    #__odamlar_soni=0
    def __init__(self,ism,faml,teln,adres,bosqich,yosh=10):
        self.ism=ism
        self.fm=faml
        self.__id=43564535
        self.teln=teln
        self.adres=adres
        self.__yosh=yosh
        self.bosqich=bosqich
        #Shahs.__odamlar_soni+=1
    def __str__(self):
    # or def __repr__(self):  ikkalasinign vazifasi bitta 
        return f"Shahsining ismi - {self.ism.title()}.\nFamiliyasi - {self.fm.title()}\n"
    def __rerp__(self):
        return f" Shahsning adressi : {self.adres}.\n Shahsning Telefon nomeri : {self.teln}.\n"
    def __lt__(self,y):
       return self.bosqich>y
    def __le__(self,y):
        return self.bosqich<y
    def __eq__(self,y):
        return self.bosqich==y
t1=Shahs("shukur","rezamonov",93,"oltinsoy",20)
t2=Shahs("Anvar","Saidov",93,"shahrisabz",65)
t3=Shahs("humoyun","otaboyev",93,"xiva",34)
t4=Shahs("asliddin","liboyev",43,"paxtachi",36)
print(t1.__str__())
print(t1.__lt__(3))
print(t1.__le__(7))
print(t1.__eq__(6))
#print(dir(Shahs))

