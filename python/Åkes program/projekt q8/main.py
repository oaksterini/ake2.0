import pygame, random, sys


class spel:
    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen_width = pygame.display.Info().current_w
        self.screen_height = pygame.display.Info().current_h

        self.spelare_y_speed = 0
        self.spelare_x_speed = 0

        self.asteroid_y_speed = 0
        self.asteroid_x_speed = 3
        self.asteroid_y = random.randint(20, self.screen_height - 19)
        self.asteroid_x = 0
    
        
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.spelare = pygame.Rect(self.screen_width/2 - 25, self.screen_height / 2 - 25, 50, 50)
        self.asteroid = pygame.Rect(self.asteroid_x, self.asteroid_y - 25, 50, 10)
    
    def spelar_animation(self):
        

        self.spelare.y += self.spelare_y_speed
        self.spelare.x += self.spelare_x_speed
        
        if self.spelare.top <= 0:
            self.spelare.top = 0
        if self.spelare.bottom >= self.screen_height:
            self.spelare.bottom = self.screen_height
        if self.spelare.left <= 0:
            self.spelare.left = 0
        if self.spelare.right >= self.screen_width:
            self.spelare.right = self.screen_width
    
    def asteroid_animation(self):
        self.asteroid.x -= self.asteroid_x_speed
        
    
    def kör(self):

        while True:
            if self.asteroid.x <= 0:
                self.asteroid.x = self.screen_width
                self.asteroid.y = random.randint(1, self.screen_height - 20)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_s:
                        self.spelare_y_speed += 7
                    if event.key == pygame.K_w:
                        self.spelare_y_speed -= 7
                    if event.key == pygame.K_d:
                        self.spelare_x_speed +=7
                    if event.key == pygame.K_a:
                        self.spelare_x_speed -= 7
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        self.spelare_y_speed -= 7
                    if event.key == pygame.K_w:
                        self.spelare_y_speed += 7
                    if event.key == pygame.K_d:
                        self.spelare_x_speed -=7
                    if event.key == pygame.K_a:
                        self.spelare_x_speed += 7
            
        
            self.spelar_animation()
            self.asteroid_animation()
                    

            
            
            
            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen,(255,255,255), self.spelare)
            pygame.draw.rect(self.screen, (255,255,255), self.asteroid)
            
            
            

            

            pygame.display.flip()
            self.clock.tick(60)

spel().kör()