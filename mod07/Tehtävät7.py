#Tehtävä_1
import random
def noppa_heittäinen():
    silmäluku=random.randint(1,6)
    return silmäluku
heitto=noppa_heittäinen()
while heitto!=6:
    print(heitto)
    heitto=noppa_heittäinen()
print(heitto)


#Tehtävä_2
import random

def noppa_heittäminen(luku):
    silmäluku=random.randint(1,luku)
    return silmäluku
tahkojen_yhteismäärä=int(input("anna tahkojen yhteismäärä: "))
heitto=noppa_heittäminen(tahkojen_yhteismäärä)
while heitto!=tahkojen_yhteismäärä:
    print(heitto)
    heitto=noppa_heittäminen(tahkojen_yhteismäärä)
print(heitto)


#Tehtävä_2(toinen tapa )
import random
def noppa_heittäminen(luku):
    silmäluku=random.randint(1,luku)
    return silmäluku
tahkojen_yhteismäärä=int(input("anna tahkojen yhteismäärä: "))

while True:
    heitto=noppa_heittäminen(tahkojen_yhteismäärä)
    print(heitto)
    if heitto==tahkojen_yhteismäärä:
        break
print(heitto)
    
#Tehtävä_3
def bensiini_määrä_litrana(luku):
    litra=luku*3.785
    return litra
gallona=int(input("anna bensiinin määrän nestegallonoina: "))
muunnos=bensiini_määrä_litrana(gallona)
while gallona!=-1:
   print(muunnos)
   gallona=int(input("anna bensiinin määrän nestegallonoina: "))
   muunnos=bensiini_määrä_litrana(gallona)
print("syöttää oikean syötten ")

#Tehtävä_3(toinen tapa)
def bensiini_määrä_litrana(luku):
    litra=luku*3.785
    return litra

while True:
    gallona=int(input("anna bensiinin määrän nestegallonoina: "))
    muunnos=bensiini_määrä_litrana(gallona)
    print(muunnos)
    if gallona==-1:
        break
print("syöttää oikean syötten ")

#Tehtävä_4:
def minun_lista(luvut):
    summa=sum(luvut)
    return summa
kokonaisluku=[1,2,3,4,5]
print(minun_lista(kokonaisluku))
#Tehtävä_5:

def minun_lista(luvut):
    toinen_lista=[]
    for i in luvut:
        if i%2==0:
            toinen_lista.append(i)
    return toinen_lista
kokonaisluku=[1,2,3,4,5,6,7,8]
print(kokonaisluku)
tulos=minun_lista(kokonaisluku)
print(tulos)

#Tehtävä_6:
import math
def pyöräen_pizza_hinta(halkaisija,hinta):
    pinta_ala=((halkaisija/2)**2)*math.pi
    per_neliömetri_hinta=hinta/pinta_ala
    return round(per_neliömetri_hinta,2)
pizza_1_hlkaisija=int(input("anna pizzan halkaisija: "))
pizza_1_hinta=int(input("anna pizzan hinta: "))
tulos_1=pyöräen_pizza_hinta(pizza_1_hlkaisija,pizza_1_hinta)
pizza_2_hlkaisija=int(input("anna pizzan halkaisija: "))
pizza_2_hinta=int(input("anna pizzan hinta: "))
tulos_2=pyöräen_pizza_hinta(pizza_2_hlkaisija,pizza_2_hinta)
print(f"ensimäisen pizzan yksikköhinta euroina per neliömetri on {tulos_1}")
print(f"toinsen pizzan yksikköhinta euroina per neliömetri on {tulos_2}")
if tulos_1<tulos_2:
    print("pizza 1 on edullisempi")
else:
    print("pizza 2 on edullisempi")