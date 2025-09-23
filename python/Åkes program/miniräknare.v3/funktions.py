import pygame, re, math
from variabler import display_text, ALLOWED_RE

def rita_text(surface, text, font, color, rect):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

def sanitize_and_eval(expr):
    # Byt symboler
    expr = expr.replace("×", "*")
    expr = expr.replace("÷", "/")
    expr = expr.replace("^", "**")

    # Ta bort dubbla mellanslag
    expr = expr.strip()

    # Enkel säkerhetskontroll: tillåt bara siffror, operatorer och parenteser
    # Efter att vi ersatt ^ med **, så innehåller uttrycket bara 0-9, +-*/(). och mellanslag
    if not expr:
        raise ValueError("Tomt uttryck")

    # För att undvika att '**' gör regex fail eftersom '*' är tillåtet så är regex okej
    if not ALLOWED_RE.match(expr.replace("**", "")):
        raise ValueError("Otillåtet tecken i uttrycket")

    # Undvik farliga konstruktioner genom att blockera två liknande bokstavssekvenser
    # men vi tillåter bara vad regex accepterar så detta är extra

    # Kör eval i en begränsad kontext
    try:
        result = eval(expr, {"__builtins__": None}, {"math": math})
    except Exception as e:
        raise
    return result


def knapp_tryck(namnlapp):
    global display_text
    if namnlapp == "C":
        display_text = 0
        return
    if namnlapp == "←":
        if len(display_text) <= 1:
            display_text = 0
        else:
            display_text = display_text[:-1]
        return
    if namnlapp == "=":
        try:
            resultat = sanitize_and_eval(display_text)
            # formatera resultat
            if isinstance(resultat, float):
                # runda där det behövs
                resultat = round(resultat, 12)
                # ta bort onödiga nollor
                resultat = int(resultat) if resultat.is_integer() else resultat
            display_text = str(resultat)
        except Exception:
            display_text = "Fel"
        return
    