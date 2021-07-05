filename='Documents\GitHub\Python_Tasks/sh.txt'
with open(filename) as file:
    for line in file:
        print(line)
talabalar=[]
with open(filename) as file:
    talabalar =file.readlines()
talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)
    pi=file.read()
pi=pi.rstrip()
pi=pi.replace('\n','')
print(pi)

filen='Documents\GitHub\Python_Tasks/new_file'
ism='Gulchiroy'
yosh=20
with open(filen,'w') as f:
    f.write(ism + '\n')
    f.write(str(yosh) + '\n')
 
with open(filen,'a') as f:
    f.write('Elinur' + '\n')
    f.write('2002'+'\n')

import pickle

file_pkl='Documents\GitHub\Python_Tasks/file.pkl'

t1={'ism':'Asalxon','maktab':'6','ism':'Elinur','maktab':'58'}
t2={'ism':'Ulug\'bek','yosh':'20','ism':'umid','yoshi':'21'}

with open(file_pkl,'wb') as f:
    pickle.dump(t1,f)
    pickle.dump(t2,f)

