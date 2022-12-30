from pygame import *

win = display.set_mode((700,500))
backgroun = transform.scale(image.load("background.jpg"),(700,500))
class Sprites():
    
    def __init__(self,Pimage,p_x,p_y,size_x, size_y,p_speed):
        super().__init__()
        self.image = transform.scale(image.load(Pimage),(size_x,size_y))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))  

class Player(Sprites):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 340:
            self.rect.y += self.speed
class Player2(Sprites):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 340:
            self.rect.y += self.speed



           
finish = True       
player1 = Player("12.png",10, 10, 30, 150, 5)
player2 = Player2("12.png",660,10,30,150,5)
ball = Sprites("ball.png",330, 230,50,50,2 )
fps = 60
clock = time.Clock()
speed_x = 4
speed_y = 4
score1 = 3
score2 = 3
font.init()
fontes = font.SysFont("Arial", 45)
fontes2 = font.SysFont("Arial", 26)
losen = fontes.render("Player 2 was lost ", 1, (250, 0, 0)) 
text_win = fontes2.render("Жизни 1 игрока : " + str(score1), 1, (255,255,255))
losen2 = fontes.render("Player 1 was lost ", 1, (250, 0, 0)) 
game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    
    

    
    if finish == True:
        win.blit(backgroun,(0,0))
        
        player2.update()
        player1.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450:
            speed_y = -1 * speed_y
        if ball.rect.y < 10:
            speed_y *= -1
    
        if sprite.collide_rect(ball, player2):
            speed_x *= -1
            speed_y *= -1
        if sprite.collide_rect(ball, player1):
            speed_y *= -1
            speed_x *= -1
    
        if ball.rect.x > 700:
            if score2 == 1:
                finish = False
                win.blit(losen, (210,230))
            if score2 > 0:
                score2 -= 1
                
                speed_x *= -1
                speed_y *= -1

                
        if ball.rect.x < 0:
            if score1  == 1:
                finish = False
                win.blit(losen2, (210,230))
            if score1 > 0:
                score1 -= 1
                
                speed_x *= -1 + 1
                speed_y *= -1 + 1
            

    text_win = fontes2.render("Жизни 1 игрока : " + str(score1), 1, (255,255,255))
    text_win2 = fontes2.render("Жизни 2 игрока : " + str(score2), 1, (255,255,255))
    win.blit(text_win,(80,10))
    win.blit(text_win2,(450,10))

    player1.reset()
    player2.reset()
    ball.reset()



    
    display.update()
    clock.tick(fps)