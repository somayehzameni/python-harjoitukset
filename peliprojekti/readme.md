# pelin nimi: 
pelastusoperatio(Maapäällinen elämä)

**Tekijä:**
Somayeh Zameni

---

## 1.  Pelin idea ja tavoite:
Tämä peli on tekstiseikailupeli. Pelin aihe liittyy kestävään kehitykseen. Pelissa on olemassa 2 aluetta : metsä ja aavikko. Alueilla on tapahtunut erilaisia kriisejä ,ja pelaaja liikkuu alueiden välillä ja ratkaisee kriisejä. Pelin tavoiteena on tehdä pelastusoperatio ja paras päätös, joka auttaa pelastamaan maapallon ja palauttaa rauha ja tasapaino ympäristöön.


---

## 2. Ominaisuudet:
-  **Interaktiivinen päävalikko:** Mikä auttaa pelaajaa ymmärtämään pelin prosessin alussa ja vaihtamaan helposti vaihtoehtojen välillä.
-  **Luettavat johdanto ja ohjetekstit:** Tarjotaan luettava ja ymmärrettävä selitys pelin alussa, mikä johtaa siihen, että pelaaja tutustuu pelinympäristöön.
-  **Inventaario-järjestelmä:** Mikä mahdollistaa kerätä erilaisia esineitä, hallita ja nähdä niitä.
-  **esineiden valmistusjärjestelmä:** Pelaaja voi luoda tarvittavia esineitä pelastusoperation tekemiseen pelin aikana.
-  **tallennus ja lataus:** Pelaaja voi tallentaa pelinsä missä tahansa pelin vaiheessa.

---


## 3. Toimintaperiaattee:
-  **Käynnistä peli ja näytä johdanto:** Kun käynnistä peli, näytetään valikot ja tulostetaan ohjeiden ja johdannon tekstit.
-  **Vlitse alue:** Pelaaja valitsee alueen, jossa hän aikoo tehdä pelastusoperaation. Sen jälkeen tulostetaan valitun alueen esittelyteksti ja näytetään alueella olevat esineet.
-  **Alueiden välillä liikkuminen:** Pelaaja voi liikkuu helposti erialueiden välilläja tarkistaa niitä.
-  **Esineiden luominen ja pelastusoperation suorittaminen:** Kun pelaaja mennee valisemaan alueen, hän pitää suorittaa pelastusoperatio esineiden yhdistelemällä. Hän luoo tarvittavia esinitä, joiden avulla voi pelasta kyseisen alueen.
- **Tallentaa ja lataa pelin:** Kun pelaaja suorittaa operatio,  hän voi tallentaa pelin ja jatkaa pelin myöhemmin tallenettusta vaiheesta.


---

## 4. Kestävä kehitys:
Pelin aihe liittyy YK:n kestävän kehityksen tavoitteeseen 15: Maan elämä (luonnon monimuotoisuuden suojelu).
Aiheen tarkoituksena on suojella maaekosysteemejä ja metsää myös edistää metsien kestävää käyttöä ja estää aavikon etenemistä.

---


## 5. Pelin kansio ja tiedostot:
Minun pelissa on yksi pääkansio, että sen sisällä on  yksi peketti ,jossä on 4 moduuliä:
- **1)Luokkien tiedosto**
- **2)Funktion tiedosto**
- **3)intro.txt tiedosto**
- **4)ohjeet.txt tiedosto**

Myös paketin ulkopuolella, pääkansiossa on "mainpeli" tiedosto ja "tallennus.json" tiedosto, jossa on kaikki tallenetut tärkeät tidot.


---

## 6. Pelin paketti:
Pelissä on yksi peketti ,jossä on 4 moduuliä:

### 1. Luokien tiedosto:
Tässä pelissä määritellään 4 tarvittavaa luokkaa. Luokat ovat seuraavat: 
- **a)Alue luokka:** Alueen luokan alustajat ovat kyseisen alueen nimi, kuvaus ja alueen oletustyökalut, jotka on lista ja listassa on esineen luokan luomaa olioita . pääohjelmassa annetaan näiden kolmen ominaisuuden arvot.  Lisäksi asetetaan 4 metodia, jotka tekevät eilaisia toimintoja.
- **b)Esine luokka:** Esine luokan alustajat ovat työkalun nimi ja käytön. Annetaan näille kahdelle ominaisuudelle arvo input_komennon avulla metsän pelastuksen ja aavikon pelastuksen funktiossa. Luokka myös sisältää metodia.

- **c)Erikoisesine luokka:** Erikoiesine luokka on alaluokka esineen luokasta. Erikoisesineen alustajat ovat sama kuin esineen luokan lisäksi luokassa on teho ominaisuus. Luokka sisältää myös esineen luokan metodin.


- **d)Pelaaja luokka:** Pelaaja luokka alustajat ovat pelaajan nimi, iän ja repun. Määritellään pelaajan nimen ja iän ominaisuuksien arvot input_komennon avulla aloitta_peli funktiossa. Mutta repun arvo on tyhjä lista. Lisäksi asetetaan erilaisia metodeja.


 ### 2. Funktion tiedosto:
Tässä pelissä käytettään erilaisia funktioita. Jotkut niistä funktiosta ova pääfunktioita ja osa niistä toimi apufunktioina. Seuraavassa todetaan pääfunktioita sekä niiden apufunktioita:
- **a)Aloitta-peli funktio:** Tässä funktiossa kysytään pelaajalta nimi ja ikä ja ohjelma tarkistaa iän ehtoa. Sen jälkeen tehdään pelaajan olio pelaajan luokasta ja myös tehdään alueen oliot alueen luokasta. Aluksi se avaa "intro.txt" tiedotoa, jossa on kirjoitettu johdantoa ja esitellä kaksi alueetta. Sen jälkeen käyttäjä on valita mille alueelle hän haluaa mennä. käyttäjän valinnan perustella määritellään kahta apufunktiota:(metsän pelastus funktio ja aavikon_etenemisen_estäminen funktio(tässä myös käytetään tarvittaessa  kaivonporaustiimi funktio.)
- **b)Päävalikko funktio:** Aluksi se tulostaa valikojen nimen ja sen jälkeen input_komennon avulla otetaan käyttäjän valitsema valikon. Tässä funktiossa käyttäjän valitsema valikon perustella määritellään 3 funktiota(1: Ohjeet funktio ,että sen toiminta on avaa"ohjeet.txt" tiedostoa ja tulosttaa ohjeet ja antaa tietoa pelistä . 2:Aloitta peli funktio(tätä funktio on mainittu aiemmin) . 3:Lataa peli funktio, että sen toiminta on lataa tallennetut tiedot ja pelaaja voi aloitta peli tästä vaiheesta)
- **c)Tallenttaa funktio:** Tätä funktio saa paremetrina pelaajan luokan luoma olio ,kaksi alueen luokan luomaa oliota ja myös nykyinen alue. Sen toiminta on se, että tallenttaa tärkeät tiedot pelistä seuraavaa kertaa varten.

### 3. Intro.txt tiedosto:
On tekstitiedosto, sinnä on kirjoitettu johdannon tekstiä.

### 4. Ohjeet.txt tiedosto:
On tekstitiedosto, sinnä on kirjoitettu ohjeen tekstiä.

