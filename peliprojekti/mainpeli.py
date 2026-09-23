from classes import Pelaaja , Alue
from functions import päävalikko_1
#Pelinnimi=Maapäällinen elämä(pelastusoperatio)
pelaajan_nimi=input("mitä sinun nimensi on? ")
pelaajan_ikä=int(input("kuinka vanha olet? "))
print(pelaajan_nimi,str(pelaajan_ikä))

if pelaajan_ikä <12:
    print("Sinä olet alle 12-vuoitias")
else :
    print("Tervetuloa peliin" , pelaajan_nimi)

    uusi_pelaaja=Pelaaja(pelaajan_nimi,pelaajan_ikä)

    metsä=Alue("metsä","Tervetuloa metsään!\n\nMetsä on häätätilassa ja tarvitsee sinun apuaisi.\n\nTällä hetkellä on tapahtunut 2 suurta kriisiä metsässä:\n1:Laaja tulipalo pohjoisessa.\n2:Puiden laiton kaato")
    aavikko=Alue("aavikko","Tervetuloa aavikkoaluelle!\n\nTällä aluella on nyt kuivaa.Sinun pitää estää maaperän kuivuminen, muuten tämän alueen maaperän tuhoutuu.\n\nTällä hetkellä on 2 suurta ongelmaa aavikkoaluella:\n1:Vakava vesipula(Veden kaivot ja vesistöt ovat kuivuneet)\n2:maaperän kuivuminen ja pensaiden tuhoutunut. )")   
    päävalikko_1(uusi_pelaaja,metsä,aavikko)




        

        
        


    

    

    




