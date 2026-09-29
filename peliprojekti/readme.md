# pelin otsikko: 
Maapäällinen elämä(pelastusoperatio)

# oma nimi:
 Somayeh Zameni

# Pelin kuvasu:
Tämä peli on tekstiseikailupeli. Pelin aihe liittyy kestävään kehitykseen. Aiheen tarkoituksena on suojella maaekosysteemejä, palauttaa niitä ennalleen ja edistää niiden kestävää käyttöä; edistää metsien kestävää käyttöä; taistella aavikoitumista vastaan; pysäyttää maaperän köyhtyminen ja luonnon monimuotoisuuden häviäminen. 

# Käyttöohjeet:

#Peli etenee vain valitsemalla valikoista sinun haluaman numeron. Tässä pelissä on olemassa kolme eri reittiä .Sinun komento määrittää pelin polkua. Sillä tekee päätöstä huolellisesti. Sinun tavoite on tehtä paras päätös, joka auttaa pelastamaan maapallon.


# 1:
#Anna nimesi ja ikäsi

# 2:
#Valitse sopivaa vaihtoehtoa päävalikosta(1: Aloita, 2:Ohjeet ,q:Lopeta)

# 3:
#Valitsemalla numero_1 eri reittiä avautuu.

# Pelinprojektti_3:

#Tässä vaiheessa minä määrittelin muutaman funktion pelille.Esimekkinä yksi funktio on kutsuttu, kun halutaan valita päävalkoista sopivaa vaihtoehtoa. Joissa tilanteissa yhden funktion sisällä on käytetty toista funktiota,tioisin sanoen ne ovet yhteydessä. Määrittelin myös yksi funktio,joka saa parametrina ja argumenttina listan.

# Pelin tiedostot:
#Minun peli koostuu kolmesta tiedostosta:
#1)Luokkien tiedosto
#2)Funktion tiedosto
#3)Mainpeli tiedostot 



#1)Luokkien tiedosto:

Tässä pelissä määritellään kolme tarvittavaa luokkaa. Luokat ovat seuraavat:

#a)Alue luokka: Alueen luokan alustajat ovat kyseisen alueen nimi ja kuvaus ja pääohjelmassa annetaan näiden kahden ominaisuuden arvot.  Lisäksi asetetaan yhden metodin ja sen nimi on tiedot. Metodin toiminta on tulostaa kuvauksen ominaisuuksien arvo .

#b)Esine luokka: Esine luokan alustajat ovat työkalun nimi ja käytön. Annetaan näille kahdelle ominaisuudelle arvo input_komennon avulla metsän pelastuksen ja aavikon pelastuksen funktiossa. Sen lisäksi asetetaan yhden metodein tässä luokassa ja sen toiminta on se että, tulostaa työkalun nimi ja käytön.
#_

#c)Pelaaja luokka: Pelaaja luokka alustajat ovat pelaajan nimi, iän, sijainnin ja repun. Määritellään       pelaajan nimen ja iän ominaisuuksien arvot input_komennon avulla pääohjelmaasa. Mutta sijainnin  arvo on aluksi None ja repun arvo on myös tyhjä lista. Lisäksi asetetaan kaksi metodia : 1) lisää esineet (sen tehtävä on lisää luodut työkalut pelaan repun listaan) 2) näyttä  esineet(sen tehtävä on näyttää repun listan tuotteet)
#_

#2) Funktion tiedosto:

#Tässä pelissä käytettään 6 funktiota. Jotkut niistä funktiosta ova pääfunktioita ja osa niistä toimi apufunktioina. Seuraavassa todetaan pääfunktioita sekä niiden apufunktioita:
 

 #a)Aloitta-peli funktio: Tätä funktio saa parametrina pelaajan luokan luoma olio ja kaksi alueen luokan luomaa oliota .Aluksi se tulostaa johdantoa ja esitellä kaksi alueetta. Sen jälkeen käyttäjä on valita mille alueelle hän haluaa mennä.käyttäjän valinnan perustella määritellään kahta apufunktiota:(1:metsän pelastus funktio 2) aavikon_etenemisen_estäminen (tässä myös käytetään tarvittaessa  kaivonporaustiimi funktio.)

 #b)Päävalikko funktio:  Tätä funktio saa parametrina  pelaajan luokan luoma olio ja kaksi alueen luokan luomaa oliota  sama kuin Aloitta_peli funktio. Aluksi se tulostaa valikon nimen ja sen jälkeen input_komennon avulla otetaan käyttäjän valitsema valikon. Tässä funktiossa käyttäjän valitsema valikon perustella määritellään kaksi funktiota(1: Ohjeet funktio että sen toiminta on se että, tulostaa ohjeet ja antaa tietoa pelistä . 2:Aloitta peli funktio)


#3)Mainpeli tiedosto:
Tässä tiedostossa ensiksi kutsutaan tarvittavat luokat ja funktiot kyseisestä tiedostosta.Sen jälkeen otetaan pelaajan nimi ja pelaajan iän input_komennon avulla. Myös  tehdään metsä ja aavikko oliot Alue luokan avulle. Sen jälkeen kutsutaan päävalikko funktio ja anettaan parametrina alueen oliot ja  pelaajan tiedot.

