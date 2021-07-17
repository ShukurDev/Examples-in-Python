# 1-task. Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
# Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
print("Eng yxshi ko'rgan kitobingizni kiriting : ")
kitob = "Istalgan kitobingizni nomini kiriting"
kitob += " (dasturmi tuxtatish uchun stop deb yozing) \n"

while True:
    qiymat = input(kitob)
    if qiymat == 'stop':
        break

print("Dastur tugadi RAHMAT")

# 2-task. Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm,
# 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin
# va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
print("Yoshingizni kiriting : ")
savol = "Istalgan son kiriting "
savol += "(dassturni tuxtatish uchun exit yoki quit ni bosing -->  \n"
yosh = True

while yosh:
    yosh = input(savol)
    if yosh == 'exit' or yosh == 'quit':
        yosh = False
        yosh = int(yosh)
    elif yosh != 'exit' and yosh != 'quit':
        yosh = int(yosh)
        if yosh < 7:
            print("Sizga chipta narxi: 2000 so/'m")
        elif yosh > 7 and yosh < 18:
            print("Sizga chipta narxi: 3000 so/'m")
        elif yosh > 18 and yosh < 65:
            print("Siz uchun chipta naerxi: 10000 so/'m")
        elif yosh > 65:
            print("siz uchun chipta narxi TEKIN")

print("Dastur tugadi.")

# 17-Lesson 3-task.Quyidagi dasturda bir nechta mantiqiy xatolar bor.
# Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?
savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:

    qiymat = input(savol)
    if qiymat == 'Exit':
        break
    elif float(qiymat) < 0:
        continue
    else:
        ildiz = float(qiymat) ** (0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
print("Dastur tugadi")