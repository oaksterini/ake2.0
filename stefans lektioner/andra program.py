#överskrift
print("-------------\nrumsberäkning\n-------------")
# Ange Längd, Bredd och Höjd

print("\n\nviktiga frågor:")

längd = float(input("vad är längden på rummet: "))
brädd = float(input("vad är brädden på rummet: "))
höjd = float(input("vad är höjden på rummet: "))
area_golv = längd*brädd
area_vägg_kort = brädd*höjd

area_vägg_lång = längd*höjd

area_vägg_tot = area_vägg_kort*2 + area_vägg_lång*2

volym_rum = area_golv*höjd
# skriv ut resultat
print("resultat")

print("area golv = ",area_golv,"\nvolym rum = ", volym_rum, "\narea vägg kortsida = ", area_vägg_kort," are vägg långsida = ", area_vägg_lång, "area vägg tot = ", area_vägg_tot)

print(f"Volym : {volym_rum:8.3f}")
