from classes import Alue ,Esine ,Pelaaja


def ohjeet():
    print("Tämä peli on tekstiseikailupeli. Peli etenee vain valitsemalla valikoista sinun haluaman numeron")
    print("*Tässä pelissä on olemassa kaksi eri reittiä .Sinun komento määrittää pelin polkua. Sillä tekee päätöstä huolellisesti.\n* Jos valitse vahingossa väärän syötteen, peli pyytää sinua syöttämään oikean syötteen.\n*Sinun tavoite on tehtä paras päätös, joka auttaa pelastamaan maapallon.")


def kaivonporaustiimi():
        print("Kavonporaustiimin puhelinnumero on: 0465892345")


def metsän_pelastus(uusi_pelaaja,metsä):
    metsä.tiedot()
    valita=input("Mitä kriisiä valitset ensin?(1-2)")
    if valita=="1":
        print("Metsässä on suuri tulipalo.Sinun tehtävä on samutttaa tulipaloa.")
        työkalu=input("mitä työkalua sinä tarvitset? ")
        käyttö=input("Mihin käytät tätä työkalua?(vastaa vähintään kahdella sanalla)")
        uusi_esine=Esine(työkalu,käyttö)

        uusi_pelaaja.lisää_esineet(uusi_esine)

        uusi_pelaaja.näyttä_esineet()
        print("Palo sammutettiin ja sinä suoritit pelastusoperaatio onnistuneesti.")
       
    if valita =="2":
        print("Metsässä kaadetaan puita laittomasti.Sinun täytyy taistella tätä toimintaa vastaan.")
        työkalu=input("mitä työkalua sinä tarvitset? ")
        käyttö=input("Mihin käytät tätä työkalua?(vastaa vähintään kahdella sanalla)")
        uusi_esine=Esine(työkalu,käyttö)
        uusi_pelaaja.lisää_esineet(uusi_esine)
        uusi_pelaaja.näyttä_esineet()
        print("sinä suoritit pelastusoperaatio onnistuneesti")

    


def aavikon_etenemisen_estäminen(uusi_pelaaja,aavikko):
    aavikko.tiedot()
    valita_2=input("Mitä kriisiä valitset ensin?")
    if valita_2=="1":
        print ("Kaikki vesikaivot ovat kuivuneet.Sinun täytyy soittaa kaivonporaustiimiin.")
        kaivonporaustiimi()
    else:
        print("Maaperä on kuivunut ja pensaat on tuhoutunut")
        komento=input("Haluatko käyttää kastelujärjestelmää?(yes or no)")
        if komento=="yes":
            katselu_esine=Esine("katselujärjestelmä","pansaiden pelastaminen")
            uusi_pelaaja.lisää_esineet(katselu_esine)
            uusi_pelaaja.näyttä_esineet()
            print("Pelastusoperaatio on tehty")
        else:
            print("Operaatio epäonnistui")

def aloitta_peli(uusi_pelaaja,metsä,aavikko):
        print("Johdanto\n \nTervetuloa!Sinut on valittu ympäristönsuojelutiimin päähenkilöksi. Tällä hetkellä maapallossa on merkittäviä kriisiä, jotka liityvät ilmastonmuutokseen. Maapallon tulevaisuus riippuu sinun päätöksesta.\n \nKaksi suurta kriisiä on tapahtunut maailmassa ja sinun on määritettävä, meille aluelle haluaat mennä ensiksi:\n 1:Metsäkato-kriisi\n 2:aavikoituma-kriisi")
        alue_1="Metsäkato-kriisi"
        alue_2="Aavikoituma-kriisi"
        komento=input("Valitse alue_1 tai alue_2")
        if komento=="alue_1":
            metsän_pelastus(uusi_pelaaja,metsä)
        
        elif komento=="alue_2":
            aavikon_etenemisen_estäminen(uusi_pelaaja,aavikko)
        


def päävalikko_1(uusi_pelaaja,metsä,aavikko):
    
       päävaliko_1="aloita peli"
       päävaliko_2="ohjeet"
       päävaliko_q="lopetttaa"
       print("Päävalikko")
       print("1:" ,päävaliko_1)
       print("2:" ,päävaliko_2)
       print("q:" ,päävaliko_q)
       päävalikko=input("Valitse komento(1-2,q): ")
       while päävalikko!="q":
           if päävalikko=="1":
               aloitta_peli(uusi_pelaaja,metsä,aavikko)
               päävalikko=input("Valitse komento(1-2,q): ")

           elif päävalikko=="2":
               ohjeet()
               päävalikko=input("Valitse komento(1-2,q): ")
       print("lopettaa,kiitos pelaamisesta")
        



    

   