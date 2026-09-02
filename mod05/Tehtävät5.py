#Tehtävä_1
luku=1
while luku <=1000:
    if luku % 3==0:
        print(luku)
    luku=luku+1

#Tehtävä_2:
tuumamäärä=float(input("anna tumat "))
while tuumamäärä>=0:
    senttimäärä=tuumamäärä*2.45
    print(str(tuumamäärä)+"tuumaa on"+str(senttimäärä)+"cm")
    tuumamäärä=float(input("anna tumat "))
print ("ohjelma lopettaa toimintansa")

#Tehtävä_3:

syöte_luku=input("anna luku")
pienin=None
suurin=None

while syöte_luku !="":
    luku=int(syöte_luku)

    if pienin is None:
        pienin=luku
        suurin=luku
    elif luku <pienin:
        pienin=luku
    elif luku >suurin:
        suurin=luku
    syöte_luku=input("anna luku")
print("pienin luku",str(pienin))
print("suuri luku",str(suurin))
    
#Tehtävä_4
import random
luku=random.randint(1,10)
arvo=int(input("anna sun arvo: "))

while arvo !=luku:
    if arvo<luku:
        print("liian pieni arvaus")
    if arvo>luku:
        print("liaan suurin arvaus")
    arvo=int(input("anna sun arvo: "))
print("oikein")

#Tehtävä_5:
käyttäjätunnus=input("anna käyttäytunnus: ")
salasana=input("anna salasana: ")

oikea_käyttätunnus="python"
oikea_salasana="rules"
virhe=0

while (käyttäjätunnus !=oikea_käyttätunnus or salasana!=oikea_salasana) and virhe<4:
    virhe=virhe+1
    print("yritä uudelleen")
    käyttäjätunnus=input("anna käyttäytunnus: ")
    salasana=input("anna salasana: ")

if käyttäjätunnus==oikea_käyttätunnus and salasana==oikea_salasana:
    print("tervetuloa")
else:
    print("pääsy evätty")
    
#Tehtävä_6:
import random
N=int(input("anna pisteiden määrää: "))
n=0
i=0
while N>i:
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if x**2 + y**2<1:
        n=n+1
    i=i+1
pii=n/N*4
print("piin likiarvo: ",float(pii))


