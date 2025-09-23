import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >=screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_score += 1
        
        score_time = pygame.time.get_ticks()
    if ball.right >=screen_width:
        opponent_score += 1
        
        score_time = pygame.time.get_ticks()

    if ball.colliderect(Player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    Player.y += player_speed
    if Player.top <= 0:
        Player.top = 0
    if Player.bottom >= screen_height:
        Player.bottom = screen_height

def opponent_animation():
    opponent.y += opponent_player_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def opponent_ai():
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom >ball.y:
        opponent.bottom -= opponent_speed

def ball_restart():
    global ball_speed_x, ball_speed_y, score_time, current_time

    
    current_time = pygame.time.get_ticks()
    
    ball.center = (screen_width/2, screen_height/2)

    if current_time - score_time < 700:
        number_three = game_font.render("3",True, light_grey)
        screen.blit(number_three,(screen_width/2+50, screen_height/2 + 20))
        screen.blit(number_three,(screen_width/2-70, screen_height/2 + 20))
    
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2",True, light_grey)
        screen.blit(number_two,(screen_width/2+50, screen_height/2 + 20))
        screen.blit(number_two,(screen_width/2-70, screen_height/2 + 20))

    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1",True, light_grey)
        screen.blit(number_one,(screen_width/2+50, screen_height/2 + 20))
        screen.blit(number_one,(screen_width/2-70, screen_height/2 + 20))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0,0
    else:
        ball_speed_y = 7 * random.choice((1,-1))
        ball_speed_x = 7 * random.choice((1,-1))
        score_time = None

    
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))


pygame.init()
clock = pygame.time.Clock()

infoObjekt = pygame.display.Info()
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong")


ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30,30,)
Player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10,140,)
opponent= pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color("grey12")
light_grey = (200,200,200)
röd = (255, 0, 0)
grön = (0, 255, 0)
blå = (0, 0, 255)

boll_färg = (light_grey)
boll_färg_nu = (boll_färg)
spelar_färg = (light_grey)
spelar_färg_nu = (spelar_färg)
opponent_färg = (light_grey)
opponent_färg_nu = (opponent_färg)

ball_speed_x = 8
ball_speed_y = 8
player_speed = 0
opponent_speed = 8
opponent_player_speed = 0

opponent_player = False


player_score = 0
opponent_score = 0
esc_text = "esc för att spela:\np för att växla mellan ai\noch tvåspelare:\nr för att starta om:\ne för exit\ns för skins"
skinsystem_text = "esc för att gå tillbaka\nR för röda skins\nb för blåa skins\ng för gröna skins"
game_font = pygame.font.Font("freesansbold.ttf",32)


score_time = True

spelar = True

esc = False

running = True
restarting = False
skinsystem = False


while running == True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and esc == False:
                esc = True
            elif event.key == pygame.K_ESCAPE and esc == True and skinsystem == False:
                esc = False
            elif event.key == pygame.K_ESCAPE and esc == True and skinsystem == True:
                esc = True
                skinsystem = False
        
            if event.key == pygame.K_p and opponent_player == False:
                opponent_player = True
            elif event.key == pygame.K_p and opponent_player == True:
                opponent_player = False
            
            if event.key == pygame.K_e and esc == True and skinsystem == False:
                pygame.quit()
                sys.exit()
            
            if event.key == pygame.K_s and esc == True and skinsystem == False:
                skinsystem = True
            
                

        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_r and esc == True and skinsystem == False:
                player_score = 0
                opponent_score = 0
                ball.center = (screen_width/2, screen_height/2)
                ball_speed_y = 7 * random.choice((1,-1))
                ball_speed_x = 7 * random.choice((1,-1))
                Player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10,140,)
                opponent= pygame.Rect(10, screen_height/2 - 70, 10, 140)
                esc = False

            

                if score_time:
                    current_time = pygame.time.get_ticks()
       
                    if current_time - score_time < 700:
                        number_three = game_font.render("3",True, light_grey)
                        screen.blit(number_three,(screen_width/2+50, screen_height/2 + 20))
                        screen.blit(number_three,(screen_width/2-70, screen_height/2 + 20))    
                    if 700 < current_time - score_time < 1400:
                        number_two = game_font.render("2",True, light_grey)
                        screen.blit(number_two,(screen_width/2+50, screen_height/2 + 20))
                        screen.blit(number_two,(screen_width/2-70, screen_height/2 + 20))
                    if 1400 < current_time - score_time < 2100:
                        number_one = game_font.render("1",True, light_grey)
                        screen.blit(number_one,(screen_width/2+50, screen_height/2 + 20))
                        screen.blit(number_one,(screen_width/2-70, screen_height/2 + 20))
                    ball_restart()
            
            if event.key == pygame.K_s and esc == True:
                skinsystem = True
            
            if event.key == pygame.K_r and esc == True and skinsystem == True:
                spelar_färg_nu = röd
                opponent_färg_nu = röd
                boll_färg_nu = röd
           
            if event.key == pygame.K_b and esc == True and skinsystem == True:
                spelar_färg_nu = blå
                opponent_färg_nu = blå
                boll_färg_nu = blå
             
            if event.key == pygame.K_g and esc == True and skinsystem == True:
                spelar_färg_nu = grön
                opponent_färg_nu = grön
                boll_färg_nu = grön
              

            

                

                
                
                
            
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                opponent_player_speed += 7
            if event.key == pygame.K_w:
                opponent_player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                opponent_player_speed -= 7
            if event.key == pygame.K_w:
                opponent_player_speed += 7


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
    
    if esc == True:
        spelar = False
    else:
        spelar = True
    
    

    if spelar:
        current_time = pygame.time.get_ticks()
        if score_time:
            if current_time - score_time < 700:
                number_three = game_font.render("3",True, light_grey)
                screen.blit(number_three,(screen_width/2+50, screen_height/2 + 20))
                screen.blit(number_three,(screen_width/2-70, screen_height/2 + 20))   
            if 700 < current_time - score_time < 1400:
                number_two = game_font.render("2",True, light_grey)
                screen.blit(number_two,(screen_width/2+50, screen_height/2 + 20))
                screen.blit(number_two,(screen_width/2-70, screen_height/2 + 20))
            if 1400 < current_time - score_time < 2100:
                number_one = game_font.render("1",True, light_grey)
                screen.blit(number_one,(screen_width/2+50, screen_height/2 + 20))
                screen.blit(number_one,(screen_width/2-70, screen_height/2 + 20))
        ball_animation()
        player_animation()
        if opponent_player == False:
            opponent_ai()
        else:
            opponent_animation()

        screen.fill(bg_color)
        pygame.draw.rect(screen,spelar_färg_nu, Player)
        pygame.draw.rect(screen,opponent_färg_nu, opponent)
        pygame.draw.ellipse(screen, boll_färg_nu, ball)
        pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))
        player_text = game_font.render(f"{player_score}",True,light_grey)
        screen.blit(player_text,(screen_width-screen_width/4,screen_height/2))

        opponent_text = game_font.render(f"{opponent_score}",True,light_grey)
        screen.blit(opponent_text,(screen_width/4,screen_height/2))

        if score_time:
            ball_restart()
    elif spelar == False and skinsystem == False:
        screen.fill(bg_color)
        pygame.draw.rect(screen,spelar_färg_nu, Player)
        pygame.draw.rect(screen,opponent_färg_nu, opponent)
        pygame.draw.ellipse(screen, boll_färg_nu, ball)
        

        player_text = game_font.render(f"{player_score}",True,light_grey)
        screen.blit(player_text,(screen_width-screen_width/4,screen_height/2))
        opponent_text = game_font.render(f"{opponent_score}",True,light_grey)
        screen.blit(opponent_text,(screen_width/4,screen_height/2))

        text = game_font.render(f"{esc_text}",True,light_grey)
        screen.blit(text,(screen_width/2 - 140,20))
    

    elif esc == True and skinsystem == True:
        screen.fill(bg_color)
        text = game_font.render(f"{skinsystem_text}",True,light_grey)
        screen.blit(text,(screen_width/2 - 120, 20))
        pygame.draw.rect(screen,spelar_färg_nu, Player)
        pygame.draw.rect(screen,opponent_färg_nu, opponent)
        pygame.draw.ellipse(screen, boll_färg_nu, ball)

    

    


    

    

    
    pygame.display.flip()

    
