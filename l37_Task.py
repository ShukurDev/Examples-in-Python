class developer:
    def __init__(self,ism,fam,yoshi,ishjoy,tajribasi,oyligi =10000):
        self.ism=ism
        self.fam=fam
        self.yoshi= yoshi
        self.ishjoy= ishjoy
        self.tajribasi = tajribasi
        self.__price=oyligi
        self.projects=[]

    def get_info(self):
        print("Dasturchi haqidagi ma'lumot bilan tanishing !!!")
        print(f"Ismi :{self.ism}\nFamiliyasi :{self.fam}\nYoshi = {self.yoshi}\nIsh joyi :{self.ishjoy}\n")
    def creat_project(self,p):
        self.projects.append(p)
        return self.projects

    def narx(self,sum):
        if sum > 0:
            self.__price+=sum  
        else:
            raise ValueError("Narxi manfiy bulishi mumkin emas!")
person1 = developer("Shukurali","Rezamonov",2002,"Tatu uf","hozircha yo'q",0)
person1.narx(100)
person1.creat_project("Kalculyator")
person1.creat_project("Son uyini")
person1.creat_project("check test codes")
person1.creat_project("online kundalik")

print(person1.get_info())
print(person1.creat_project("Platforma"))   