#Pelinnimi=Maapäällinen elämä(pelastusoperatio)

pelastus_esine=[]
def metsän_pelastus():
    print("Tervetuloa metsään!\n\nMetsä on häätätilassa ja tarvitsee sinun apuaisi.\n\nTällä hetkellä on tapahtunut 2 suurta kriisiä metsässä:\n1:Laaja tulipalo pohjoisessa.\nPuiden laiton kaato:")
    valita=input("Mitä kriisiä valitset ensin?(1-2)")
    if valita=="1":
        print("Metsässä on suuri tulipalo.Sinun tehtävä on samutttaa tulipaloa.")
        tulos_1=minun_lista(pelastus_esine)

        listan_tulostaminen(tulos_1)
        print("Palo sammutettiin ja sinä suoritit pelastusoperaatio onnistuneesti.")
    elif valita=="2":
      print("Metsässä kaadetaan puita laittomasti.Sinun täytyy taistella tätä toimintaa vastaan.")  
      tulos_1=minun_lista(pelastus_esine)
      listan_tulostaminen(tulos_1)
      print("sinä suoritit pelastusoperaatio onnistuneesti")
        
def aavikon_etenemisen_estäminen():
    print("Tervetuloa aavikkoaluelle!\n\nTällä aluella on nyt kuivaa.Sinun pitää estää maaperän kuivuminen, muuten tämän alueen maaperän tuhoutuu.\n\nTällä hetkellä on 2 suurta ongelmaa aavikkoaluella:\n1:Vakava vesipula(Veden kaivot ja vesistöt ovat kuivuneet)\n2:maaperän kuivuminen ja pensaiden tuhoutunut. )")
    valita_2=input("Mitä kriisiä valitset ensin?")
    if valita_2=="1":
        print ("Kaikki vesikaivot ovat kuivuneet.Sinun täytyy soittaa kaivonporaustiimiin.")
        kaivonporaustiimi()
    else:
        print("Maaperä on kuivunut ja pensaat on tuhoutunut")
        komento=input("Haluatko käyttää kastelujärjestelmää?(yes or no)")
        if komento=="yes":
            print("Pelastusoperaatio on tehty")
        else:
            print("Operaatio epäonnistui")


def luonnon_monimuotoisuuden_pelastus():
    print("Tervetuloa luonnonsuojelualueelle!\n\nAluen luonnon monimuotoisuus on hätätilassa ja luonnonvaraiset eläimet tarvitsevat sinun apuaisi.\n\nTällä hetkellä luonnossa on 2 suurta ongelmaa.\n1:Metsästäjien luvaton pääsy suojelualuelle\n2:Vesilähteiden ja elintarvikkeiden saastuminen")
    valitse_3=input("Mitä kriisiä valitset ensin?")
def minun_lista(lista):
    työkalu=input("mitä työkalua sinä tarvitset? ")
    while työkalu!="":
        pelastus_esine.append(työkalu)
        työkalu=input("mitä työkalua sinä tarvitset? ")

    return lista

def listan_tulostaminen(lista_2):
    for item in lista_2:
        if len(lista_2)!=0:
            print(item)
        else:
            print("Sinulla ei ole tavaroita")
def kaivonporaustiimi():
    print("Kavonporaustiimin puhelinnumero on: 0465892345")

def aloitta_peli():
    print("Johdanto\n \nTervetuloa!Sinut on valittu ympäristönsuojelutiimin päähenkilöksi. Tällä hetkellä maapallossa on merkittäviä kriisiä, jotka liityvät ilmastonmuutokseen. Maapallon tulevaisuus riippuu sinun päätöksesta.\n \nKolme suurta kriisiä on tapahtunut maailmassa ja sinun on määritettävä, meille aluelle haluaat mennä ensiksi:\n 1:Metsäkato-kriisi\n 2:aavikoituma-kriisi\n 3:Luonnon monimuotoisuuden kriisi")
    alue_1="Metsäkato-kriisi"
    alue_2="Aavikoituma-kriisi"
    alue_3="Luonnon monimuotoisuuden kriisi"
    komento=input("Valitse alue(1-3)")
    if komento=="alue_1":
        metsän_pelastus()
    elif komento=="alue_2":
        aavikon_etenemisen_estäminen()
    elif komento=="alue_3":
        luonnon_monimuotoisuuden_pelastus()
def päävalikko_1():
    päävaliko_1="aloita peli"
    päävaliko_2="ohjeet"
    päävaliko_q="lopetttaa"
    print("Valitse komento(1-2,q)")
    print("1:" ,päävaliko_1)
    print("2:" ,päävaliko_2)
    print("q:" ,päävaliko_q)
    päävalikko=input("Valitse komento(1-2,q): ")
    if päävalikko=="1":
        aloitta_peli()
    elif päävalikko=="2":
        print("Tämä peli on tekstiseikailupeli. Peli etenee vain valitsemalla valikoista sinun haluaman numeron")
        print("*Tässä pelissä on olemassa kolme eri reittiä .Sinun komento määrittää pelin polkua. Sillä tekee päätöstä huolellisesti.\n* Jos valitse vahingossa väärän syötteen, peli pyytää sinua syöttämään oikean syötteen.\n*Sinun tavoite on tehtä paras päätös, joka auttaa pelastamaan maapallon.")
        päävalikko=input("Valitse komento(1-2,q): ")
    else:
        print("lopettaa,kiitos pelaamisesta")
    return päävalikko
    
pelaajan_nimi=input("mitä sinun nimensi on? ")
pelaajan_ikä=int(input("kuinka vanha olet? "))
print(pelaajan_nimi,str(pelaajan_ikä))

if pelaajan_ikä <12:
    print("Sinä olet alle 12-vuoitias")
elif pelaajan_ikä>=12:
    print("Tervetuloa peliin" , pelaajan_nimi)
    while True:
        tulos=päävalikko_1()
        if tulos=="q":
            break 
    

    

    




