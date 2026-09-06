# kaupungit=["helsinki","espoo","vantaa"]
# kaupungit.append("turku")
# print(kaupungit)
# kaupungit.remove("helsinki")
# print(kaupungit)
# kaupungit.insert(1,"tampere")
# print(kaupungit)
# nimi=["somi","zahra","leila"]
# kaupungit.extend(nimi)
# print(kaupungit)
# if "somi" in kaupungit:
#     print("löytty")
# kaupungit.sort()
# print(kaupungit)
# nimet=[]
# nimi=input("anna nimi tai lopetta painamalla enter")
# while nimi !="":
#     nimet.append(nimi)
#     nimi=input("anna seurava nimi tai lopettaa painamalla enter")
# print(nimet)
# for nimi in nimet:
#     print(f"möi, {nimi}")

import random
määrä=int(input("anna arpakuutioiden lukumäärä"))

summa=0
for i in random(määrä):
    heitto=random.random(1,6)
    summa=summa+heitto
print(f"summa on: {summa}")
