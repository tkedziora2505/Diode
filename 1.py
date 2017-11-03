class Diode(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        
    def wyswietl(self):
        print(self.r, self.g, self.r)
        
    def setColour(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        
class ElementSekwencji(object):
    def __init__(self,x, time):
        self.x = x
        self.time = time
        
    def get(self, x):
        print(self.x.r, self.x.g, self.x.b, self.time)
        
class Sekwencja(object):
    ElementySekwencji = []
    def __init__(self,x):
        self.ElementySekwencji.append(x)
    
    def dodaj(self, x):
        self.ElementySekwencji.append(x)
    
    def wyswietl(self):
            print(self.ElementySekwencji) 
        
        
dioda1 = Diode(50,40,30)
dioda2 = Diode(100,150,200)
sekwencja1 = ElementSekwencji(dioda1, 70)
sekwencja2 = ElementSekwencji(dioda2, 10)
calosc = Sekwencja(sekwencja1)
calosc.dodaj(sekwencja2)
calosc.wyswietl()

