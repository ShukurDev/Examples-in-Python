# Python_Tasks

import random as r
while True:
  print("Keling o'ylagan sonni topish o'ynaymiz!")
  son = r.randint(1,10)
  print("1 dan 10 gacha son o'yladim topa olasizmi ?: ")
  n=0
  while True:
    son1=int(input())
    n+=1
    if son1<son:
       print("Xato,men o'ylagan son bundan kattaroq. Yana harakat qiling: ")
       continue
    elif son1>son:
       print("Xato,men o'ylagan son bundan kachikroq. Yana harakat qiling: ")
       continue
    else:
        print(f"TOPDINGIZ!. {son} sonini o'ylagan edim. {n} taxmin bilan topdingiz .TABRIKLAYMAN !!! \n")
        break

  son2=r.randint(1,10)
  print("1 dan 10 gacha son o'ylang men topishga harakat qilaman.\n")
  input("Son o'ylagan bulsangiz istalgan tugmani bosing va ENTERni bosing.\n")
  p=0
  while True:
    p+=1
    son3=input(f"Siz {son2} sonini o'yladingiz: To'g'ri(T),  Men o'ylagan son bundan kattaroq (+), yoki kichikroq (-) :" )
    
    if son3=='+':
      son2=r.randint(son2,10)
      continue  
    elif son3=='-':
        son2=r.randint(1,son2)
        continue
    elif son3 == 'T':
        if p==n:
          print(f"Durrang! Ikkimiz {p} ta taxmin bilan topdik.")
          break
        elif p<n:
          
          print(f"Men yutdim! Soningizni {p} taxmin bilan topdim.")
          print(f"Siz {n} ta taxmin bilan toptingiz.")
          break
        else:
          print(f"Siz Yutdingiz! Men uylagan sonni {n} ta taxmin bilan topdingiz")
          print(f"Men {p} ta taxmin bilan topdim.")
          break
  jv=input("Yana o'ynaymizmi ha(1)/yo'q(0) : ")
  if jv == 1:
     continue
  else:
    break    
     











