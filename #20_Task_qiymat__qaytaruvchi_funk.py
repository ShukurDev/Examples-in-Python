# 1-2-3-Task

def use(n,s,b,p,e='',ph=''):
    person={
          'Name':n,
          'Surname':s,
          'Born year':b,
          'Place born':p,
          'Email':e,
          'Phone number':ph
        }
    return person

print("You can enter Personal information !!!")
name=input("Enter you names: ")
surname=input("Enter you surname: ")
born=input("Enter you born year: ")
place_born=input("Enter you place born>: ")
email=input("Enter you email: ")
phone=int(input("Enter you phone number: "))

person1=[use(name,surname,born,place_born,email,phone)]
print("Foydalanuvchi haqida to'liq ma'lumot !1!\n")
for person in person1:
    print(f"Foydalanuvchining ismi: {person['Name']} \nFoydalanuvchining familiyasi: {person['Surname']}\n Foydalanuvchining tug'ilgan yili: {person['Born year']}\n Foydalanuvchining tug'ilgan joyi : {person['Place born']}\n Foydalanuvchining elektron pochta manzili : {person['Email']}\n Foydalanuvchining telefon raqami : {person['Phone number']}")


# 6-Task .Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi
# sonlar ro'yxatni qaytaruvchi funksiya yozing.  Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga
# teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi.
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

n = int(input())
def fib(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fib(a - 1) + fib(a - 2)
for i in range(1, n + 1):
    print(fib(i))







