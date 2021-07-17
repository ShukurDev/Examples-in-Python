# 1-task.Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
def multiply(*son):
    p=1
    for i in son:
        p*=i
    return p
print(multiply(1,2,3,4,55,6,776,65,546,976))

# 3-Task.Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
# Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar
# esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

def info(ism,familiya,**malumotlar):
    malumotlar['ism']=ism,
    malumotlar['familiya']=familiya
    return malumotlar
inform = info('Shukurali','Rezamonov',yoshi=19,kurs=2,ish=None)
print(inform)