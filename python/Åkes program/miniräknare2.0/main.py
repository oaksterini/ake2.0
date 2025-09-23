resultat = "Error"

räknesätt = input("Vilket räknesätt vill du använd? *, /, +, -, < eller >?\n")

if räknesätt == "*":
    S1 = int(input("Vilken siffra vill du gångra?\n"))
    S2 = int(input("Vilken siffra vill du gångra med?\n"))
    
    resultat = S1 * S2

elif räknesätt == "/":
    S1 = int(input("Vilken siffra vill du dela?\n"))
    S2 = int(input("Vilken siffra vill du dela med?\n"))
    
    resultat = S1 / S2

elif räknesätt == "+":
    S1 = int(input("Vilken siffra vill du addera?\n"))
    S2 = int(input("Vilken siffra vill du addera med?\n"))
    
    resultat = S1 + S2

elif räknesätt == "-":
    S1 = int(input("Vilken siffra har du?\n"))
    S2 = int(input("Vilken siffra vill du substrahera med?\n"))
    
    resultat = S1 - S2

elif räknesätt == "<":
    S1 = int(input("Vilken siffra har du?\n"))
    S2 = int(input("Vilken siffra vill du jämföra med?\n"))
    
    resultat = bool(S1 < S2)

elif räknesätt == ">":
    S1 = int(input("Vilken siffra har du?\n"))
    S2 = int(input("Vilken siffra vill du jämföra med?\n"))
    
    resultat = bool(S1 > S2)

elif räknesätt == ">=":
    S1 = int(input("Vilken siffra har du?\n"))
    S2 = int(input("Vilken siffra vill du jämföra med?\n"))
    
    resultat = bool(S1 >= S2)

elif räknesätt == "<=":
    S1 = int(input("Vilken siffra har du?\n"))
    S2 = int(input("Vilken siffra vill du jämföra med?\n"))
    
    resultat = bool(S1 <= S2)



print("ditt resultat är: ", resultat)


