# Quyidagi dasturimiza biz foydalanuvchi va kompyuter urtasida bullaigan uyin dasturini uzdik.
# Izoh: 1- urinda kompyuter  son uylaydi biz uni topishga harakat qillamiz va
# keyin biz son uylaymiz kompyuter u sonni topishga harakat qiladi oxirida natijalarni taqqoslab km yutganligini aytadi.

import random as r
#n=int(input())

def son_top(a=10):
    k=0
    son1=r.randint(1,a)
    print(f"Men 1 dan {a} gacha son o'yladim topa olasizmi.\n")
    while True:
        b=int(input())
        k=k+1
        if son1>b:
            print("Xato !. Men o'ylagan son bundan kattaroq.")
            continue
        elif son1<b:
            print("Xato !. Men o'ylagan son bundan kichikroq")
            continue
        else:
            print("Siz men o'ylagan sonni topdingiz.TABRIKLAYMAN!.\n")
            print(f"Siz sonni {k} ta urinish bilan topdingiz. ")
            break
    return k
#son_top()
def son_top_pc(c=10):
    l=0
    yuqori = c
    quyi = 1
    input(f"1 dan {c} gach son o'ylang va istalgan tugmani bosing  .Men topishga harakat qilaman.")
    while True:
        l=l+1
        if yuqori != quyi:
            taxminga = r.randint(quyi,yuqori)
        else:
            taxminga = quyi
        javob = input(f" Siz {taxminga} sonini o'yladingiz.To'g'ri(T) ,bundan kattaroq(+), Bundan kichikroq(-)")
        if javob == '+':
            quyi= taxminga+1
        elif javob =='-':
            yuqori =taxminga -1
        else:
            break
    print(f"Men  {l} ta taxmin bilan topdim.")
    return l
 
#son_top_pc()
def play(x=10):
    yana = True
    while yana:
        user = son_top(x)
        pc = son_top_pc(x)
        if user > pc:
            print(f"siz {user} ta taxmin bilan topdingiz va yutdingiz !")
        elif user<pc:
            print(f"Men yutdim {pc} ta taxmin bilan topdim.!")
        else:
            print(f"Durrang!. Ikkalamiz ham {user} ta taxmin bilan topdik.")
        yana = input("Yana uynaymizmi --> ha(1)/yo'q(0): ")
play()
#son_top_pc(20)
#m=int(input())
#son_top_pc(m)
