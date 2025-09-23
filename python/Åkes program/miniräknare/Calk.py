#ÅkES Miniräknare:

#Importera grejer
import pygame
import sys
import math
import re

#Starta pygame
pygame.init()

# Fönster
WIDTH, HEIGHT = 420, 560
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Miniräknare")

# Färger (RGB)
BG = (30, 30, 30)
BTN = (50, 50, 50)
BTN_HOVER = (80, 80, 80)
TEXT = (230, 230, 230)
ACCENT = (70, 130, 180)

FONT = pygame.font.SysFont(None, 36)
FONT_SMALL = pygame.font.SysFont(None, 24)
FONT_LARGE = pygame.font.SysFont(None, 48)

# Display
display_text = "0"

# Knappar: lista med rader (för layout)
buttons = [
    ["C", "←", "√", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "^", "="],
]

# Knappstorlek
PAD = 10
cols = 4
rows = len(buttons)
button_w = (WIDTH - PAD * (cols + 1)) // cols
button_h = (HEIGHT - 180 - PAD * (rows + 1)) // rows  # lämna plats för display

# Utility: rita text centrerad

def draw_text(surface, text, font, color, rect):
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect(center=rect.center)
    surface.blit(text_surf, text_rect)


# Säker utvärdering - enkel validering och eval
ALLOWED_RE = re.compile(r"^[0-9+\-*/().\s]*$")


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


# Rita hela UI

def draw_ui(mouse_pos):
    SCREEN.fill(BG)

    # Display-område
    display_rect = pygame.Rect(PAD, PAD, WIDTH - 2 * PAD, 140)
    pygame.draw.rect(SCREEN, BTN, display_rect, border_radius = 8)

    # Visa text (högerjusterad)
    txt = display_text
    # om för lång, skala ned font
    disp_font = FONT_LARGE
    while disp_font.size(txt)[0] > display_rect.width - 20 and disp_font.get_height() > 16:
        # skala ner font genom att byta till en mindre storlek
        size = disp_font.get_height() - 2
        disp_font = pygame.font.SysFont(None, size)

    txt_surf = disp_font.render(txt, True, TEXT)
    txt_rect = txt_surf.get_rect()
    txt_rect.right = display_rect.right - 12
    txt_rect.centery = display_rect.centery
    SCREEN.blit(txt_surf, txt_rect)

    # Rita knappar
    for r, row in enumerate(buttons):
        for c, label in enumerate(row):
            x = PAD + c * (button_w + PAD)
            y = display_rect.bottom + PAD + r * (button_h + PAD)
            rect = pygame.Rect(x, y, button_w, button_h)

            # hover-effekt
            if rect.collidepoint(mouse_pos):
                color = BTN_HOVER
            else:
                color = BTN

            # accent-färg för vissa knappar
            if label in ("=", "C"):
                pygame.draw.rect(SCREEN, ACCENT, rect, border_radius=10)
            else:
                pygame.draw.rect(SCREEN, color, rect, border_radius=10)

            # rita label
            draw_text(SCREEN, label, FONT, TEXT, rect)

    # liten instruktion
    help_rect = pygame.Rect(PAD, HEIGHT - 40, WIDTH - 2 * PAD, 30)
    help_surf = FONT_SMALL.render("√ tar kvadratroten av aktuell siffra.", True, (180, 180, 180))
    help_rect.topleft = (PAD + 4, HEIGHT - 36)
    SCREEN.blit(help_surf, help_rect)


# Hantera knapptryck

def on_button_press(label):
    global display_text

    if label == "C":
        display_text = "0"
        return
    if label == "←":
        if len(display_text) <= 1:
            display_text = "0"
        else:
            display_text = display_text[:-1]
        return
    if label == "=":
        # utvärdera
        try:
            result = sanitize_and_eval(display_text)
            # formatera resultat
            if isinstance(result, float):
                # runda där det behövs
                result = round(result, 12)
                # ta bort onödiga nollor
                result = int(result) if result.is_integer() else result
            display_text = str(result)
        except Exception:
            display_text = "Fel"
        return

    if label == "√":
        # Ta kvadratroten av det aktuella talet
        try:
            val = float(display_text)
            if val < 0:
                display_text = "Fel"
            else:
                res = math.sqrt(val)
                # rensa onödiga decimaler
                res = round(res, 12)
                res = int(res) if float(res).is_integer() else res
                display_text = str(res)
        except Exception:
            display_text = "Fel"
        return

    # annars: bygg uttrycket (siffror eller operatorer)
    # ersätt initial "0" när vi skriver en siffra eller punkt
    if display_text == "0" and label not in ("+", "-", "×", "÷", "^"):
        display_text = label
    else:
        # undvik två operatorer i rad (enkelt filter)
        if display_text and display_text[-1] in "+-*/^×÷" and label in "+-*/^×÷":
            # ersätt sista operator med ny
            display_text = display_text[:-1] + label
        else:
            display_text += label


# Hitta knapp under position

def button_at_pos(pos):
    display_rect = pygame.Rect(PAD, PAD, WIDTH - 2 * PAD, 140)
    for r, row in enumerate(buttons):
        for c, label in enumerate(row):
            x = PAD + c * (button_w + PAD)
            y = display_rect.bottom + PAD + r * (button_h + PAD)
            rect = pygame.Rect(x, y, button_w, button_h)
            if rect.collidepoint(pos):
                return label
    return None


# Huvudloop

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                btn = button_at_pos(event.pos)
                if btn:
                    on_button_press(btn)
            elif event.type == pygame.KEYDOWN:
                # grundläggande tangentbordsstöd
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    on_button_press("←")
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    on_button_press("=")
                else:
                    key = event.unicode
                    # matcha vissa tecken
                    if key in "0123456789.+-*/()":
                        # visa * och / som × ÷? vi använder interna symboler i display
                        display_key = key
                        if key == "*":
                            display_key = "×"
                        if key == "/":
                            display_key = "÷"
                        on_button_press(display_key)
                    elif key == "^":
                        on_button_press("^")

        draw_ui(mouse_pos)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
