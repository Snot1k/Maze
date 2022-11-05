from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys_pressed[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 700 - 85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -=self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, width, height, color1, color2, color3, x, y):
        super().__init__()
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((700, 500))
display.set_caption('Лабіринт')

background = transform.scale(image.load("background.jpg"), (700, 500) )
hero = Player("hero.png", 5, 500-80, 3)
monster = Enemy("cyborg.png", 700-80, 280, 2)
final =  GameSprite("treasure.png", 700-120, 500-80, 0)
wall_1 = Wall(450, 10, 110, 225, 165, 100, 20)
wall_2 = Wall(365, 10, 110, 225, 165, 100, 480)
wall_3 = Wall(10, 350, 110, 225, 165, 100, 20)
wall_4 = Wall(10, 370, 110, 225, 165, 200, 110)
wall_5 = Wall(10, 350, 110, 225, 165, 300, 20)
wall_6 = Wall(10, 370, 110, 225, 165, 455, 110)
wall_7 = Wall(70, 10, 110, 225, 165, 300, 370)
wall_9 = Wall(70, 10, 110, 225, 165, 390, 250)
wall_10 = Wall(70, 10, 110, 225, 165, 300, 110)
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

game = True
clock = time.Clock()
fps = 60

finish = False

font.init()

font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        hero.update()
        hero.reset()
        monster.reset()
        monster.update()
        final.reset()
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        wall_5.draw_wall()
        wall_6.draw_wall()
        wall_7.draw_wall()
        wall_9.draw_wall()
        wall_10.draw_wall()
    if sprite.collide_rect(hero, monster) or sprite.collide_rect(hero, wall_1) or sprite.collide_rect(hero, wall_2) or sprite.collide_rect(hero, wall_3) or sprite.collide_rect(hero, wall_4) or sprite.collide_rect(hero, wall_5) or sprite.collide_rect(hero, wall_6) or sprite.collide_rect(hero, wall_7) or sprite.collide_rect(hero, wall_9) or sprite.collide_rect(hero, wall_10):
           finish = True
           window.blit(lose, (200, 200))
           kick.play()
    if sprite.collide_rect(hero, final):
           finish = True
           window.blit(win, (200, 200))
           money.play()
    display.update()
    clock.tick(fps)