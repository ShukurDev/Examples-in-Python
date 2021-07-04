import json
# 1- Task
# data = {"Model" :"Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# x_json=json.dumps(data)
# print(x_json)

# 2-Task
talaba_json = {"ism":"Hasan","familiya":"Husanov","tyil":2000}
talaba=json.loads(talaba_json)
print(talaba)
#print(f"Ismi : {talaba['ism']}\nFamiliyasi :{talaba['familiya']}")