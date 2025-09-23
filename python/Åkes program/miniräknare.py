import os
import sys

def restart():
    print('Restarting script...')

    os.execv(sys.executable, ['python'] + sys.argv)

print("Åkes miniräknare.py\n\n")



räknesätt = input("vilket räknesätt vill du använda\n")




print("Välj ditt ")

    

first = input("första:\n")
second = input("andra:\n")
print("nummer\n")

summan = float(first) + float(second)
differensen = float(first) - float(second)
produkten = float(first) * float(second)
kvoten = float(first) / float(second)

if räknesätt == "*":
    print("Svaret är " + str(produkten))
elif räknesätt == "+":
    print("Svaret är " + str(summan))
elif räknesätt == "-":
    print("Svaret är " + str(differensen))
elif räknesätt == "/":
    print("Svaret är " + str(kvoten))

else:
    print("error\n")
    restart()
    




if input("Vill du använda miniräknaren igen j/n\n") == ("j" or "J"):
    print("vad bra :)")
    restart()
    
else:
    quit()




