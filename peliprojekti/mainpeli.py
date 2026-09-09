#Pelinnimi=Maapäällinen elämä(pelastusoperatio)
pelaajan_nimi=input("mitä sinun nimensi on? ")
pelaajan_ikä=int(input("kuinka vanha olet? "))
print(pelaajan_nimi,str(pelaajan_ikä))

if pelaajan_ikä <12:
    print("Sinä olet alle 12-vuoitias")
else:
    print("Tervetuloa peliin" , pelaajan_nimi)
    päävaliko_1="aloita peli"
    päävaliko_2="ohjeet"
    päävaliko_q="lopetttaa"
    print("Valitse komento(1-2,q)")
    print("1:" ,päävaliko_1)
    print("2:" ,päävaliko_2)
    print("q:" ,päävaliko_q)
    päävalikko=input("Valitse komento(1-2,q): ")
    while päävalikko!="q":
        if päävalikko=="1":
            print("Johdanto\n \nTervetuloa!Sinut on valittu ympäristönsuojelutiimin päähenkilöksi. Tällä hetkellä maapallossa on merkittäviä kriisiä, jotka liityvät ilmastonmuutokseen. Maapallon tulevaisuus riippuu sinun päätökseen.\n \nKolme suurta kriisiä on tapahtunut maailmassa ja sinun on määritettävä, meille aluelle haluaat mennä ensiksi:\n 1:Metsäkato-kriisi\n 2:Metsäkato-kriisi\n 3:Luonnon monimuotoisuuden kriisi")
            alue_1="Metsäkato-kriisi"
            alu_2="Aavikoituma-kriisi"
            ale_3="Luonnon monimuotoisuuden kriisi"
            komento=input("Valitse alue(1-3)")
        elif päävalikko=="2":
            print(päävaliko_2)

            print("Tämä peli on tekstiseikailupeli. Peli etenee vain valitsemalla valikoista sinun haluaman numeron")
            print("*Tässä pelissä on olemassa kolme eri reittiä .Sinun komento määrittää pelin polkua. Sillä tekee päätöstä huolellisesti.\n* Jos valitse vahingossa väärän syötteen, peli pyytää sinua syöttämään oikean syötteen.\n*Sinun tavoite on tehtä paras päätös, joka auttaa pelastamaan maapallon.")
        päävalikko=input("Valitse komento(1-2,q): ")
    print("lopettaa,kiitos pelaamisesta")
        


