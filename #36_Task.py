# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya
# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya
# Berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya
# Berilgan son Fibonachchi ketma-ketligida uchraydimi (True) yoki yo'q (False) qaytaruvchi funksiya yozing.

def katta(a,b,c):
    s=max(a,b,c)
    return s


def matn(m):
    return m.title()

def fibonachi(n):
    if n==0  or n==1:
        return 1 
    else:
         return fibonachi(n-1)+fibonachi(n-2)

k=int(input())
for i in range(1,k+1):
    print(fibonachi(i))

