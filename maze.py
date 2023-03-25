from pygame import *

win_width = 700
win_height = 500
font.init()
font=font.SysFont('Arial',32)
text=font.render('YOU WON',True,(111,222,222))


window = display.set_mode((win_width, win_height))
display.set_caption("Maze99")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

class Sprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed

        self.rect = self.image.get_rect()

        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    
class Player(Sprite):
    def move(self):
        keys=key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 636:
            self.rect.x += self.speed
        if keys[K_DOWN] and self.rect.y < 458:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y < 350:
            self.rect.y -= self.speed

class Enemy(Sprite):
    direction = "left"

    def move(self):
        if self.rect.x < 400:
            self.direction = 'right'
        if self.rect.x > 650:
            self.direction= 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self,rgb,x,y,w,h):
        super(). __init__()
        self.rgb=rgb
        self.widht=w
        self.height = h




        self.wall = Surface((w,h))
        self.wall.fill(rgb)
        
        self.rect = self.wall.get_rect()
        self.rect.x=x
        self.rect.y=y

    def draw(self):
        window.blit(self.wall,(self.rect.x,self.rect.y))

player = Player('hero.png', 1, 80, 4)
monster = Enemy('cyborg.png', 80, 280, 2)
final = Sprite('treasure.png', 620,400, 2)



w1 = Wall ((111,121,222),300,30,10,200)
w2 = Wall ((111,121,222),20,20,500,10)
w3 = Wall ((111,121,222),300,350,10,150)
w4 = Wall ((111,121,222),300,350,250,10)
w5 = Wall ((111,121,222),0,350,300,10)
w6 = Wall ((111,121,222),300,218,250,10)





game = True
clock = time.Clock()
FPS = 60

#музика
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background,(0, 0))
    
    player.reset()
    player.move()
    monster.move()
    monster.reset()
    if sprite.collide_rect(player,monster)\
        or sprite.collide_rect(player,w1)\
        or sprite.collide_rect(player,w2)\
        or sprite.collide_rect(player,w3)\
        or sprite.collide_rect(player,w4)\
        or sprite.collide_rect(player,w5):
         player.rect.y=70
         player.rect.x=20
            
    if sprite.collide_rect(player,final):
        window.blit(text, (500,200))
    w1.draw()
    w2.draw()
    w3.draw()
    w4.draw()
    w5.draw()
    w6.draw()
    final.reset()
    display.update()
    clock.tick(FPS)