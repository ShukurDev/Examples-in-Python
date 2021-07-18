#  1 - Task   .Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar
# (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)
class Avtomobil:
    def __init__(self,model,rang,narx,karobka,yyuli=0):
        self.model = model
        self.rang=rang
        self.narx=narx
        self.box=karobka
        self.kilometr=yyuli

    def get_info(self):
      return f"Avtomobilning modeli : {self.model}.\nRang :{self.rang}\nNarxi = {self.narx}.\nHollati :{self.box}"

n1=Avtomobil("nexia","qizil",10000,"Aftomat")
n2=Avtomobil("captiva","sariq",40000,"Mexanik")
print(n1.get_info())
print(n2.get_info())


# 2 - Task  . Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
# get_info() metodi avti haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
class Avtomobil:
    def __init__(self,model,rang,narx,karobka,yyuli=0):
      self.model = model
      self.rang=rang
      self.narx=narx
      self.box=karobka
      self.kilometr=yyuli
     # self.ism=ism
      #self.familiya=familiya

    def get_info(self):
      return f"Avtomobilning modeli : {self.model}.\nRang :{self.rang}\nNarxi = {self.narx}.\nHollati :{self.box}"
    def get_name(self):
        return self.rang
   # def get_lastname(self):
    #    return f" Mijozimizning ismi : {self.ism}\nFamiliyasi:{self.familiya}"
n1=Avtomobil("nexia","qizil",10000,"Aftomat")
n2=Avtomobil("captiva","sariq",40000,"Mexanik")
print(n1.get_info())
print(n2.get_info())
print(n1.get_name())
#print(n1.get_lastname())


# 3 - Task .Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
# update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin

class Avtomobil:
    def __init__(self, model, rang, narx, karobka, km=1):
        self.model = model
        self.rang = rang
        self.narx = narx
        self.box = karobka
        self.km = km

    def get_info(self):
        return f"Avtomobilning modeli : {self.model}.\nRang :{self.rang}\nNarxi = {self.narx}.\nHollati :{self.box}\n Yurgan yuli: {self.km}"

    def update_km(self):
        self.km += 1

    # def get_lastname(self):
    #   return f" Mijozimizning ismi : {self.ism}\nFamiliyasi:{self.familiya}"


n1 = Avtomobil("nexia", "qizil", 99996, "Aftomat")
n2 = Avtomobil("captiva", "sariq", 40000, "Mexanik")

print(n1.get_info())
print(n2.get_info())



#4 - Task .Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring
# (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)
class avtosalon:
  def __init__(self,s_nomi,manzili):
    self.nom=s_nomi
    self.manzil=manzili
    self.sss=10
    self.soni=0
    self.avtos=[]
  def add_avtos(self,avto):
    self.avtos.append(avto)
    self.soni+=1
    return f"O'zbekistonning {self.manzil} tumanida  {self.nom} - rusumli avtolar soni->{self.sss} ta\nAvtosalondagi yangi kelgan avtomobillar ruyhati{self.avtos} \nYangi kelgan avtolar soni:{self.soni}"
aftomobil=avtosalon("Nexia","Oltinsoy")
aftomobil.add_avtos("captiva")
aftomobil.add_avtos("malibu")
aftomobil.add_avtos("damas")
aftomobil.add_avtos("lambargino")
print(aftomobil.add_avtos("ferrari"))


#5-Task.  Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing
class infor:
    def __init__(self, nomi, narxi, rangi, karobkasi, yili):
        self.nom = nomi
        self.narx = narxi
        self.rang = rangi
        self.box = karobkasi
        self.yil = yili

    def get_info(self):
        return f"Avtosalondagi {self.nom} rusumli mashinamizning narxi : {self.narx} so'm.\nMashinamizning rangi -->{self.rang},\nKarobkasi = {self.box}\nZavoddan chiqqan yili = {self.yil}"


car2 = infor("Nwxia", 45000000, "qaymoq", "mexanik", 2008)
car = infor("Captiva", 250000000, "oq", "avtomat", 2015)
print(car.get_info())
print(car2.get_info())


# 6- Task .Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring
class infor:
    def __init__(self, nomi, narxi, rangi, karobkasi, yili):
        self.nom = nomi
        self.narx = narxi
        self.rang = rangi
        self.box = karobkasi
        self.yil = yili

    def get_info(self):
        return f"Avtosalondagi {self.nom} rusumli mashinamizning narxi : {self.narx} so'm.\nMashinamizning rangi -->{self.rang},\nKarobkasi = {self.box}\nZavoddan chiqqan yili = {self.yil}"


car2 = infor("Nwxia", 45000000, "qaymoq", "mexanik", 2008)
car = infor("Captiva", 250000000, "oq", "avtomat", 2015)
print(dir(infor))
print(car2.__dict__)
print(car.__dict__.keys())