import json
#1- Task
data = {"Model" :"Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
x_json=json.dumps(data)
print(x_json)

#2-Task
talaba_json = {"ism":"Hasan","familiya":"Husanov","tyil":2000}
talaba=json.dumps(talaba_json)
print(f"Ismi : {talaba_json['ism']}\nFamiliyasi :{talaba_json['familiya']}")

#3-Task

with open('talaba.json','w') as f:
    json.dump(x_json,f)
with open('talabalar1.json','w') as f1:
    json.dump(x_json,f1)

#4- Task
filename='Downloads/students.json'
with open(filename) as f:
   talaba1=json.load(f)
print(f"Ismi : {talaba1[0]['name']} \nFamiliyasi : {talaba1[0]['lastname']}. \n")
print(talaba1)