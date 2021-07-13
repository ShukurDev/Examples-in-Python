# Quyidagi o'zgaruvchilarni yarating: 
kocha=input("Ko'changizni kiriting :")
mahalla=input("Mahallangizni kiriting : ")
tuman=input("Tumaniningizni kiriting : ") 
viloyat=input("Viloyatingizni kiriting : ")

manzil = f"{kocha.capitalize()}  ko'chasi\n{mahalla.capitalize()}  mahallasi\n{tuman.capitalize()} tumani\n{viloyat.capitalize()}  villoyati."

print(manzil.upper(),"\n")
print(manzil.title(),"\n")
print(manzil.lower(),"\n")