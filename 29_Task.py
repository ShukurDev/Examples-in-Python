class Avtomobil:
    def __init__(self,model,rang,narx):
        self.model = model
        self.rang=rang
        self.narx=narx

    def get_name(self):
        return self.model
n1=Avtomobil("nexia","qizil",10000)
print(n1.get.name())

