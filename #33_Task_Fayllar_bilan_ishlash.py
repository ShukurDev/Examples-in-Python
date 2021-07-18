
file1= 'Documents\GitHub\Python_Tasks/learn.txt'
# 1-Task
with open(file1) as file:
    t=file.read()
print(t)

# 2-Task
# yu8klab olindi fayl

# 3-Task
def tekshir(n):
    if n=='20020714':
        print("yes")
    else:
        print("No")

fl ='Downloads/pi_million_digits.txt'
with open(fl) as k:

    t1 =k.read()
t1=t1.rstrip()
t1=t1.replace('\n','')
tekshir(t1)


# 4-Task
import pickle
file_pkl='Documents\GitHub\Python_Tasks/file.pkl'
with open(file_pkl,'rb') as f:
    t1=pickle.load(f)
    t2=pickle.load(f)
print(t1)
print(t2)

# 5-Task
filename = 'Documents\GitHub\Python_Tasks/sh.txt'
with open(filename) as file:
    for line in file:
        print(line)
talabalar = []
with open(filename) as file:
    talabalar = file.readlines()
talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)
pi = file.read()
pi = pi.rstrip()
pi = pi.replace('\n', '')
print(pi)

#6 - Task
filen = 'Documents\GitHub\Python_Tasks/new_file'
ism = 'Gulchiroy'
yosh = 20
with open(filen, 'w') as f:
    f.write(ism + '\n')
    f.write(str(yosh) + '\n')

with open(filen, 'a') as f:
    f.write('Elinur' + '\n')
    f.write('2002' + '\n')

#9-Task
import pickle

file_pkl = 'Documents\GitHub\Python_Tasks/file.pkl'

t1 = {'ism': 'Asalxon', 'maktab': '6', 'ism': 'Elinur', 'maktab': '58'}
t2 = {'ism': 'Ulug\'bek', 'yosh': '20', 'ism': 'umid', 'yoshi': '21'}

with open(file_pkl, 'wb') as f:
    pickle.dump(t1, f)
    pickle.dump(t2, f)

