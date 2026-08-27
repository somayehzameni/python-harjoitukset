# Muuttujat ja vuorovaikutteiset ohjelmat 
#
user=input("annaa niminsi")
eka = -9
toka = 12_456_123_180
kolmas = 4.973
neljäs = -4 + 2j

print(eka)
print(toka)
print(kolmas)
print(neljäs)
print(neljäs.real)
print(neljäs.imag)
# #example 1
radius_of_circle=input("radius of circle: ")
sid_length_of_square=input("sid length of square")
import math
print (float(radius_of_circle)**2 *math.pi )
print (float (sid_length_of_square)**2 *math.pi)
#example 2
amount_of_banana=input("give me the amount of banana: ")
amount_of_apple=input ("give me the amount of apple: ")
amount_of_orange=input ("give me the amount of orange: ")
banana_price=2.58
apple_price=3.15
orange_price=4.05
print (int (amount_of_banana )* banana_price)
print (int (amount_of_apple) * apple_price)
print (int(amount_of_orange) * orange_price)
print (int (amount_of_banana )* banana_price + int (amount_of_apple) * apple_price + int(amount_of_orange) * orange_price)
import random 
random_1= random.randint(1,6)
random_2= random.randint(1,20)
print (int(random_1))
print (int(random_2))
