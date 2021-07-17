# 19-lesson 1-TASK
def t_yil(ism, yosh):
    ''' Foydalanuvchining nechi yoshdaligini qaytaruvchi funksiya
    '''
    print(f"{ism.title()} sizning yoshingiz {2021 - yosh}  da")
print("Hurmatli mijoz shahsiy ma'lumotingizni kiriting: ")
a = str(input("Ismingizni kiriting: "))
b = int(input("tug'ulgan yilingizni kiritng :"))
t_yil(a, b)


#19-lesson 2-TASK
n=int(input("Istalgan soningizni kiriting : "))
def kvadrat(n):
    '''Kiritilgan sonning kcadrati va kubini chiqaradi
    '''
    print(f"Kiritilgan sonning kvadrati = {n*n}\n"
          f"Kiritilgan sonning kubi = {n*n*n}")
kvadrat(n)


#19-lesson 5-TASK
def juftoq(x,y=2):
    ''' Sonning n-darajasini topuvchi funksiya
    '''
    print(f"Kiritilgan sonning n-darajasi = {x*y}")
x,y=map(int,input().split())
juftoq(x,y)


#19-lesson 7-TASK
n=int(input())
def tekshr(n):
    for i in range(2,11):
       if n%i==0:
          print(f"{n} {i} ga qoldiqsiz bo'linadi.")
       else:
          continue
tekshr(n)

