#tehtävä 1 
seasons=("spring","summer","faal","winter")
number=int(input("please write a number"))
if number in (3,4,5):
    print (seasons[0])
elif number in (6,7,8):
    print(seasons[1])
elif number in (9,10,11):
    print(seasons[2])
elif number in (12,1,2):
    print(seasons[3])
#tehtävä_2
name=input("please write name ")
name_1=set()
while name!="":
    if name in name_1:
        print("Existing name")
    else:
        name_1.add(name)
        print("New name")
    name=input("please write name ")
for i in name_1:
    print(i)
print(name_1)


numerot={"somi":"0465897861","zahra":"0466109281"}
numerot["olga"]="0919526673"
print(numerot)
name=input("enter name ")
if name in numerot:
    print(numerot[name])
autot=[{"malli":"toyota","väri":"ghermez","hinta":"3450"},{"malli":"benz","väri":"sabz","hinta":"23589"}]
print(autot[0])
print(autot[1]["malli"])
for i in autot:
    print(i)
    

#Tehtävä-3:
lentoasaman_tiedot={}
while True:
    komento=input("syöttää sinun komennon: 1=uusi lentoasema, 2=tieto haku, 3=lopetta")
    if komento=="1":
        nimi=input("annaa lentoaseman nimi: ")
        koodi=input("annaa lentoaseman ICAO koodi: ")
        lentoasaman_tiedot[koodi]=nimi
    elif komento=="2":
        koodi=input("annaa lentoaseman ICAO koodi: ")
        print(lentoasaman_tiedot[koodi])
    elif komento=="3":
        break
    
