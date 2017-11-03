class Colour(object):
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
        
        
niebieski = Colour(255,255,255)
czerwony = Colour(255,255,0)
sekwencja1 = ElementSekwencji(czerwony, 70)
sekwencja2 = ElementSekwencji(niebieski, 10)
dioda1 = Sekwencja(sekwencja1)
dioda2.dodaj(sekwencja2)
calosc.wyswietl()

