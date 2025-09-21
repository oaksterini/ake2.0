
# Importera alla nödvändiga bibliotek
import math


# Överskrift
print("------------------")
print("deg : cos : sin")


#Tabell
for deg in range(0,91,5):
    rad = deg * math.pi/180
    c   = math.cos(rad)
    s   = math.sin(rad)
    print(f"{deg:3d} {c :6.3f} {s :6.3f}")
#underskrift (del av överskrift)
print("------------------")
