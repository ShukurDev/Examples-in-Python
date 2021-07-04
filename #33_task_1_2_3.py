#file1= 'Documents\GitHub\Python_Tasks/learn.txt'
# 1-Task
# with open(file1) as file:
#     t=file.read()
# print(t)

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
