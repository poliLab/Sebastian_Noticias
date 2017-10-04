import requests
from estractor import estractor
from lector import lector

class crawly:
    def __init__(self, seed=None):
        self.seed=seed or []
        
            
    

    def obtenersemillas(self):
         a=open("minacion", "r")
         seeds=a.read().splitlines()
         a.close()
         return seeds


estract=estractor("http://www.eltiempo.com/")
html=estract.obtenerhtml()

lect=lector(html)
tags=lect.obtenertag("a")
for tag in tags:
	print(tag.get('href'))
	#dict((k.encode('ascii'),v) for(k,v) in tag.attrs )


	








#l=crawly()






#seeds = l.obtenersemillas()
#for seed in seeds: print(seed)

#l=crawly("https://www.google.com.co/")
#p=l.obtenerhtml()
#print (p.text)
