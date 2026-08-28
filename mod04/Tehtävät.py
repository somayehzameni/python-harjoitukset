#Tehtävä_1
kuha_pituus=int(input("Anna kuhan pituus:"))
alamittanen=37
if kuha_pituus<alamittanen:
    puutuu=alamittanen - kaha_pituus
    print ("sinun pitäisi palautta kuha järveen koska sallitusta pyyntimitasta puuttuu"+ str(puutuu ))

#Tehtävä_2
hyttiluokka=input("mikä hyttiluokka sopii teille? ")
lux_hyttiluokka="lux on parvelleellinen hytti yläkannella"
a_hyttiluokka="on ikkunnallinen hytti autokannen yläpuolella"
b_hyttiluokka="on ikkunnaton hytti autokannan yläpuolella"
c_hyttiluokka="on ikkunaton hytti autokannen alapuolella"
if hyttiluokka =="Lux":
   print(lux_hyttiluokka)
elif hyttiluokka=="A":
    print(a_hyttiluokka)
elif hyttiluokka=="B":
    print(b_hyttiluokka)
elif hyttiluokka=="C":
    print(c_hyttiluokka)
else:
    print("virheellinen hyttiluokka")

#Tehtävä_3

Sukupuoli=input("Mikä sinun biologisen sukupuoli? ")
Hemogolobiiniarvo=int(input("Mikä sinun hemogolobiiniarvo? "))
if Sukupuoli=="nainen" and 117<=Hemogolobiiniarvo<=175:
    print("homogolobiiniarvo on normaali")
elif Sukupuoli=="nainen" and Hemogolobiiniarvo>175:
    print("hemogolobiiniarvo on korkea")
elif Sukupuoli=="nainen" and Hemogolobiiniarvo<117:
    print("hemogolobiiniarvo on alhainen")
elif Sukupuoli=="mies" and 134<=Hemogolobiiniarvo<=195:
    print("homogolobiiniarvo on normaali")
elif Sukupuoli=="mies" and Hemogolobiiniarvo>=195:
    print("hemogolobiiniarvo on korkea")
elif Sukupuoli=="mies" and Hemogolobiiniarvo<=134:
    print("hemogolobiiniarvo on alhainen")

