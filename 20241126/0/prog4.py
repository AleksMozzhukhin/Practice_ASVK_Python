import pickle


class SerCls:
    def __init__(self, l,d,n,s):
        self.lst=list(l)
        self.dct=dict(d)
        self.num=int(n)
        self.st=str(s)
    def __str__(self):
        return "  ||  ".join([str(self.lst),str(dict(self.dct.items())),str(self.num),self.st])

s=SerCls([1,6,2,"werg"],{2:"qwer"},3,"booo")

d=pickle.dumps(s)
del s
ser1=pickle.loads(d)
print(ser1)