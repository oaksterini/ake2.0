#ÅkES Miniräknare:
#importera och starta pygame
import pygame as pg
pg.init()

#Importera grejer
import sys
import math
import re






# Fönster
from variabler import screen
pg.display.set_caption("Miniräknare")

# Färger (RGB)
from variabler import bg, knapp, knapp_hover, text, accent, mörkröd

#textstorlek/font
from variabler import font_stor, font_mellan, font_liten


#import till rita ui
from variabler import bredd, höjd, knappar, knappar_höjd, knappar_bredd, rad, columner, tio
from funktions import rita_text


#rita ui
def rita_ui(mus_pos):
    screen.fill(bg)
    display_rekt = pg.Rect(10,10, bredd-20, höjd/7)
    pg.draw.rect(screen,mörkröd,display_rekt)
    for r, rad in enumerate(knappar):
        for c, namnlapp in enumerate(rad):
            x = tio + c * (knappar_bredd + tio)
            y = display_rekt.bottom + tio + r * (knappar_höjd + tio)
            rect = pg.Rect(x, y, knappar_bredd, knappar_höjd)
            if rect.collidepoint(mus_pos):
                färg = knapp_hover
            else:
                färg = knapp
            pg.draw.rect(screen, färg, rect)
            rita_text(screen, namnlapp, font_mellan, text, rect)
            
    return namnlapp
    







#main funktion och loop
def main():
    running = True
    clock = pg.time.Clock()
    #main loop
    while running:
        #hämta muspekarens position och lägg den i variabeln mus_pos
        mus_pos = pg.mouse.get_pos()
        #gör det möjligt att stänga programmet
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False


        #Rita nästa frame
        rita_ui(mus_pos)        
        pg.display.flip()
        #fps
        clock.tick(60)
    #Stäng av
    pg.quit()
    sys.exit()

main()

