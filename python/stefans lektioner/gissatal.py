#importera bibliotek

import random

#bestäm facit
facit = random.randint(0,100)

#game loop
Running = True
antal_gissningar = 0

while Running:
    gissning = int(input("gissa ett tal mellan 0 och 100\n"))
    antal_gissningar += 1

    if gissning == facit:
        Running = False
    elif gissning < facit:
        print("Högre\n")
    else:
        print("lägre\n")

#grattis
print("grattis du gissade", antal_gissningar, "gånger")



