import random

antal_ettor = 0
antal_tvåer = 0

for x in range(0,600):
    tal =random.randint(1,6)
    if (tal == 1):
        antal_ettor += 1
            
    elif (tal ==2):
        antal_tvåer += 1

    
    print(tal, end =" ")

print ("antalet ettor: ", antal_ettor)
print ("antalet tvåor: ", antal_tvåer)

