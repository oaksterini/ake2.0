#Importera moduler
import pygame,re


#fönster
bredd, höjd = 420, 560
screen = pygame.display.set_mode((bredd, höjd))
#fönsterinnehåll
knapp_storlek = 10

# Färger (RGB)
bg = (30, 30, 30)
knapp = (50, 50, 50)
knapp_hover = (80, 80, 80)
text = (230, 230, 230)
accent = (70, 130, 180)
mörkröd = (30, 0, 0)

#fonter och fontstorlek
font_mellan = pygame.font.SysFont(None, 36)
font_liten = pygame.font.SysFont(None, 24)
font_stor = pygame.font.SysFont(None, 48)

#Lista mes knappar i 
knappar = [
    ["(", ")", "%", "√"],
    ["C", "←", "π", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "^", "="],
    ]

#knappstorlek
rad = len(knappar)
columner = 5
knappar_bredd = (bredd/4)-11.75
knappar_höjd = (höjd/10)
tio = 10

#texten i rutan
display_text = 0

#tillåtna tecken
ALLOWED_RE = re.compile(r"^[0-9+\-*/().\s]*$")

