class foydalanuvchi:
    def __init__(self,ism,familiya,email,login,yosh,tyil,tjoy,tnom):
        self.name =ism
        self.familiya= familiya
        self.email=email
        self.login=login
        self.tyil=tyil
        self=t_joy=tjoy
        self.tnom=tnom


while True:
    ismr=input("Foydalanuvchining ismini kiriting: ")
    fm=input("Foydalanuvchining familiyasini kiriting: ")
    em=input("Foyalanuvchining e-manzilini kiriting: ")
    lg=int(input("Foyalanuvhcining loginni kiriting: "))
    tn=int(input("Foydallanuchining tel nomrini kiting: "))
    ty=int(input("Foyalanuchining tug'ilgan yilini kiriting: "))
    tj=input("Foydalanuchining tug'ilgan joyini kiting : ")
    user=foydalanuvchi(ismr,fm,em,lg,tn,ty,tj)
    jv=input("yana foydalanuvchi qushishni hohlaysizmi: ha/yoq : ")
    if jv=='ha':
        continue
    else:
        print(user)
        break
