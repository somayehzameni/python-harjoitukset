#Tehtävä _1
user=input("annaa nimesi")
print ("Tervetulua" + user)

#Tehtävä_2
ympäryn_sääteen=input("annaa ympäryn sääteen: ")
import math
ympäryn_pinta_ala= (int(ympäryn_sääteen)**2 * math.pi)
print (f"ympäryn pinta ala: {ympäryn_pinta_ala: .2f}")


Tehtävä_3
suorakulmio_kanta=input("annaa suorakulmion kanta")
suorakulmio_korkeus=input ("annaa suorakulmion korkeus")
suorakulmio_pinta_ala= (int(suorakulmio_kanta)* int(suorakulmio_korkeus))
suorakulmio_piiri=(int(suorakulmio_kanta)+int(suorakulmio_korkeus)*2)
print(f"Suorakulmion pinta ala: {suorakulmio_pinta_ala: .2f}")
print(f"Suorakulmion piiri: {suorakulmio_piiri: .2f}")

#Tehtävä_4
ensimäinen_luku=input("annaa ensimäinen luku")
toinen_luku=input("annaa toinen luku")
kolmas_luku=input("anna kolmas luku")
lukujen_summa=(int(ensimäinen_luku)+int(toinen_luku)+int(kolmas_luku))
lukujen_tulo=(int(ensimäinen_luku)*int(toinen_luku)*int(kolmas_luku))
lukujen_keskiarvo=(int(ensimäinen_luku)+int(toinen_luku)+int(kolmas_luku) /3)
print(f"lukujen summa: {lukujen_summa}")
print(f"lukujen tulos: {lukujen_tulo}")
print(f"lukujen keskiarvo: {lukujen_keskiarvo}")

Tehtävä_5


leiviskä_muoto=input("annaa leiviskät")
naula_muoto=input("annaa naulat")
luoti_muoto=input("annaa luodit")
leiviskat_gramma=(float(leiviskä_muoto)*20*32*13.3)
naulat_gramma=(float(naula_muoto)*32*13.3)
luodit_gramma=(float(luoti_muoto)*13.3)
kokonaisgramma=(float(leiviskat_gramma)+float(naulat_gramma)+float(luodit_gramma))
kilogramma=(int(kokonaisgramma)//1000)
gramma=(float(kokonaisgramma)%1000)
print(f"kilogramma {kilogramma} ja gramma {gramma: .3f} ")

#Tehtävä_6

import random
numero_1=random.randint(1,9)
numero_2=random.randint(1,9)
numero_3=random.randint(1,9)

print(str(numero_1)+str(numero_2)+str(numero_3))

k_1=random.randint(1,6)
k_2=random.randint(1,6)
k_3=random.randint(1,6)
k_4=random.randint(1,6)

print(str(k_1)+str(k_2)+str(k_3)+str(k_4))
