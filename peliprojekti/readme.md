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
#Valitse sopivaa vaihtoehtoa päävalikosta(1: Aloita peli , 2:laata peli , 3:ohjeet ,q:Lopeta)

# 3:
#Valitsemalla numero eri reittiä avautuu.

# Pelinprojektti_3:

#Tässä vaiheessa minä määrittelin muutaman funktion pelille.Esimekkinä yksi funktio on kutsuttu, kun halutaan valita päävalkoista sopivaa vaihtoehtoa. Joissa tilanteissa yhden funktion sisällä on käytetty toista funktiota,tioisin sanoen ne ovet yhteydessä. Määrittelin myös yksi funktio,joka saa parametrina ja argumenttina listan.

# Pelin kansio ja tiedostot:
Minun pelissa on yksi pääkansio, että sen sisällä on  yksi peketti ,jossä on 4 moduuliä:
    1)Luokkien tiedosto
    2)Funktion tiedosto
    3)intro.txt tiedosto
    4)ohjeet.txt tiedosto

Myös paketin ulkopuolella, pääkansiossa on "mainpeli" tiedosto ja "tallennus.json" tiedosto, jossa on tallennettu kaikki tärkeät tidot.

# Pelin paketti:
Pelissä on yksi peketti ,jossä on 4 moduuliä:

1)Luokkien tiedosto:

Tässä pelissä määritellään 4 tarvittavaa luokkaa. Luokat ovat seuraavat:

a)Alue luokka: Alueen luokan alustajat ovat kyseisen alueen nimi, kuvaus ja alueen oletustyökalut, jotka on lista ja listassa on esineen luokan luomaa olioita . pääohjelmassa annetaan näiden kolmen ominaisuuden arvot.  Lisäksi asetetaan 4 metodia, jotka tekevät eilaisia toimintoja: 1) tiedot(sen tehtävä on tulosttaa alueen kuvauksen) 2) näyttä_aluen_esine(sen tehtävä on tulosttaa alueen esineet) 3)otta_esine_alueelta(sen tehtävä on tarvittaessaa poisttaa esineet alueelta) 4) lisää_esine_alueen(sen tehtävä on lisää esineet alueen ,jos pelaaja haluaa)

b)Esine luokka: Esine luokan alustajat ovat työkalun nimi ja käytön. Annetaan näille kahdelle ominaisuudelle arvo input_komennon avulla metsän pelastuksen ja aavikon pelastuksen funktiossa. Sen lisäksi asetetaan yhden metodein tässä luokassa ja sen toiminta on se että, tulostaa työkalun nimi ja käytön.

c)Erikoisesine luokka: Erikoiesine luokka on alaluokka esineen luokasta. Alueen alustajat ovat sama kuin esineen luokan lisäksi luokassa on teho ominaisuus. Luokka sisältää myös esineen luokan metodin.


d)Pelaaja luokka: Pelaaja luokka alustajat ovat pelaajan nimi, iän ja repun. Määritellään pelaajan nimen ja iän ominaisuuksien arvot input_komennon avulla aloitta_peli funktiossa. Mutta repun arvo on tyhjä lista. Lisäksi asetetaan kaksi metodia : 1) lisää esineet (sen tehtävä on lisää luodut työkalut pelaan repun listaan) 2) remove_esine_repusta(sen tehtävä on poistaa esineen repusta). 3) näyttä  esineet(sen tehtävä on näyttää repun listan tuotteet)


 2)Funktion tiedosto:

Tässä pelissä käytettään erilaisia funktioita. Jotkut niistä funktiosta ova pääfunktioita ja osa niistä toimi apufunktioina. Seuraavassa todetaan pääfunktioita sekä niiden apufunktioita:
 

 a)Aloitta-peli funktio: Tässä funktiossa kysytään pelaajalta nimi ja ikä ja ohjelma tarkistaa iän ehtoa. Sen jälkeen tehdään pelaajan olio pelaajan luokasta ja myös tehdään alueen oliot alueen luokasta. Aluksi se avaa "intro.txt" tiedotoa, jossa on kirjoitettu johdantoa ja esitellä kaksi alueetta. Sen jälkeen käyttäjä on valita mille alueelle hän haluaa mennä. käyttäjän valinnan perustella määritellään kahta apufunktiota:(1:metsän pelastus funktio  2) aavikon_etenemisen_estäminen (tässä myös käytetään tarvittaessa  kaivonporaustiimi funktio.)

 b)Päävalikko funktio: Aluksi se tulostaa valikojen nimen ja sen jälkeen input_komennon avulla otetaan käyttäjän valitsema valikon. Tässä funktiossa käyttäjän valitsema valikon perustella määritellään 3 funktiota(1: Ohjeet funktio ,että sen toiminta on avaa"ohjeet.txt" tiedostoa ja tulosttaa ohjeet ja antaa tietoa pelistä . 2:Aloitta peli funktio(tätä funktio on mainittu aiemmin) . 3:Lataa peli funktio, että sen toiminta on lataa tallennetut tiedot ja pelaaja voi aloitta peli tästä vaiheesta)

c)Tallenttaa funktio: Tätä funktio saa paremetrina pelaajan luokan luoma olio ,kaksi alueen luokan luomaa oliota ja myös nykyinen alue. Sen toiminta on se, että tallenttaa tärkeät tiedot pelistä seuraavaa kertaa varten.


3)Intro.txt tiedosto: On tekstitiedosto, sinnä on kirjoitettu johdannon tekstiä.

4)Ohjeet.txt tiedosto: On tekstitiedosto, sinnä on kirjoitettu ohjeen tekstiä.

