# -*- coding: utf-8 -*- 
import pygame as pg
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller 虛擬資料夾
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Button_go(pg.sprite.Sprite):
    def __init__(self, w, h):
        super().__init__()
        self.image_nor = pg.image.load(resource_path("image//go.png")).convert()
        self.image_nor.set_colorkey((255,255,255))
        self.image_nor = pg.transform.scale(self.image_nor, (w, h))
        self.rect = self.image_nor.get_rect()
        self.rect.center = (400,400)
        self.width = w
        self.height = h 
        self.image = self.image_nor 
        
    def go(self):
        global playing
        playing = 1      
        sound_go.play()
        clearGroups()
        createLevel(level)
        
        
    def update(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            self.rect.center = (400,400)
            self.image = pg.transform.scale(self.image_nor, (int(self.width*1.1), int(self.height*1.1)))
            if pg.mouse.get_pressed()[0]:
                self.go()
        else:
            self.rect.center = (410,405)
            self.image = pg.transform.scale(self.image_nor, (self.width, self.height))
            
class Map(pg.sprite.Sprite):

    def __init__(self, level):
        super().__init__()
        self.level = level
        self.image = pg.image.load(resource_path(f"image//lv{level}.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (400,300)
        self.mask = pg.mask.from_surface(self.image)
        
    def update(self):
        pass
         
class Spring(pg.sprite.Sprite):
    def __init__(self, x, y, size=(100,100)):
        super().__init__()
        self.image_nor = pg.image.load(resource_path("image//spring_nor.png")).convert()
        self.image_nor.set_colorkey(WHITE)
        self.image_nor = pg.transform.scale(self.image_nor, size)
        self.image_pre = pg.image.load(resource_path("image//spring_pre.png")).convert()
        self.image_pre = pg.transform.scale(self.image_pre, size)
        self.image_pre.set_colorkey(WHITE)
        self.image = self.image_nor
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

    def update(self):
        if pg.sprite.collide_rect(self, player):
            self.image = self.image_pre
            if player.jump_times == 0:
                if player.live:
                    sound_jump.play()
                player.jump_times = 17
        else:
            self.image = self.image_nor

class Nail(pg.sprite.Sprite):
    def __init__(self, x, y, nailtype , size):
        super().__init__()
        self.image = pg.image.load(resource_path("image//nail.png")).convert()
        self.image.set_colorkey(WHITE)
        self.image = pg.transform.scale(self.image, size)
        if nailtype.lower() == "n":
            pass
        elif nailtype.lower() == "e":
            self.image = pg.transform.rotate(self.image, -90)
        elif nailtype.lower() == "s":
            self.image = pg.transform.rotate(self.image, 180)
        else:
            self.image = pg.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mask = pg.mask.from_surface(self.image)
        
    def update(self):
        pass

class Fallnail(pg.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pg.image.load(resource_path("image//fallnail.png")).convert()
        self.image.set_colorkey(WHITE)
        self.image = pg.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.mask = pg.mask.from_surface(self.image)
        self.speed = speed
        self.y_start = y
        
    def update(self):
        self.y += self.speed
        if self.rect.midtop[1] > 600:
            self.y = self.y_start
        self.rect.center = (self.x, self.y)
        
class Enemy(pg.sprite.Sprite):
    def __init__(self, x1, x2, y, speed):
        super().__init__()
        self.image = pg.image.load(resource_path("image//enemy.png")).convert()
        self.image.set_colorkey(WHITE)
        self.image = pg.transform.scale(self.image, (90,90))
        self.rect = self.image.get_rect()
        self.rect.center = (x1, y)
        self.x = x1
        self.y = y
        self.x1 = x1
        self.x2 = x2
        self.mask = pg.mask.from_surface(self.image)
        self.way = 1 #1向右 -1右左
        self.speed = speed
        
    def update(self):
        self.x += self.speed*self.way
        if self.x < self.x1 or self.x > self.x2:
            self.way *= -1
        self.rect.center = (self.x, self.y)
        
class Flygroundx(pg.sprite.Sprite):
    def __init__(self, x1, x2, y, speed):
        super().__init__()
        self.image = pg.image.load(resource_path("image//flyground.png")).convert()
        self.image.set_colorkey(WHITE)
        self.image = pg.transform.scale(self.image, (130,130))
        self.rect = self.image.get_rect()
        self.rect.center = (x1, y)
        self.x = x1
        self.y = y
        self.x1 = x1
        self.x2 = x2
        self.speed = speed
        self.way = 1 #1向右 -1右左
        self.mask = pg.mask.from_surface(self.image)
        
    def update(self):
        self.x += self.speed*self.way
        if self.x < self.x1 or self.x > self.x2:
            self.way *= -1
        self.rect.center = (self.x, self.y)

class Flygroundy(pg.sprite.Sprite):
    def __init__(self, x, y1, y2, speed):
        super().__init__()
        self.image = pg.image.load(resource_path("image//flyground.png")).convert()
        self.image.set_colorkey(WHITE)
        self.image = pg.transform.scale(self.image, (130,130))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y1)
        self.x = x
        self.y = y1
        self.y1 = y1
        self.y2 = y2
        self.speed = speed
        self.way = 1 #1向右 -1右左
        self.mask = pg.mask.from_surface(self.image)
        
    def update(self):
        self.y += self.speed*self.way
        if self.y > self.y1 or self.y < self.y2:
            self.way *= -1
        self.rect.center = (self.x, self.y)

class Player(pg.sprite.Sprite):
    def __init__(self, xstart, ystart):
        super().__init__()
        self.image_stop = pg.image.load(resource_path("image//player_stop.png")).convert()
        self.image_stop.set_colorkey(WHITE)
        self.image_fla = pg.image.load(resource_path("image//player_fla.png")).convert()
        self.image_fla.set_colorkey(WHITE)
        self.image_l = pg.image.load(resource_path("image//player_l.png")).convert()
        self.image_l.set_colorkey(WHITE)
        self.image_r = pg.image.load(resource_path("image//player_r.png")).convert()
        self.image_r.set_colorkey(WHITE)
        self.image_die = pg.image.load(resource_path("image//player_die.png")).convert()
        self.image_die.set_colorkey(WHITE)
        self.image = pg.transform.scale(self.image_stop, (80,80))
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.xystart = (xstart, ystart)
        self.speed_x = 16 #自訂
        self.speed_jump = 30 #自訂
        self.speed_fall = 15 #自訂
        self.live = True
        self.jump_times = 0
        self.x = xstart
        self.y = ystart
        self.flashing = False        
        
        self.start()        
        
    def start(self):
        self.jump_times = 0
        self.x = self.xystart[0]
        self.y = self.xystart[1]
        self.rect.center = self.xystart
        self.flashing = False
        self.mask = pg.mask.from_surface(self.image)
        self.live = True
        
    def restart(self):
        self.jump_times = 0
        self.x = self.xystart[0]
        self.y = self.xystart[1]
        self.rect.center = self.xystart
        self.flashing = True
        self.mask = pg.mask.from_surface(self.image)
        self.live = True
        
    def die(self):
        sound_die.play()
        self.image = self.image = pg.transform.scale(self.image_die, (80,80))
        self.mask = pg.mask.from_surface(self.image)
        self.live = False
        
    def movel(self):
        self.image = pg.transform.scale(self.image_l, (80,80))
        self.mask = pg.mask.from_surface(self.image)
        if pg.sprite.spritecollide(hitbox_l, ground_sprites, False, collided = pg.sprite.collide_mask) or (self.x < 20):
            pass
        else:
            self.x -= self.speed_x
    
    def mover(self):
        self.image = pg.transform.scale(self.image_r, (80,80))
        self.mask = pg.mask.from_surface(self.image)
        if pg.sprite.spritecollide(hitbox_r, ground_sprites, False, collided = pg.sprite.collide_mask):
            pass
        else:
            self.x += self.speed_x
        
    def jumping(self):
        if pg.sprite.spritecollide(hitbox_u, ground_sprites, False, collided = pg.sprite.collide_mask):
            self.jump_times = 0
        else:
            if self.jump_times > 0:
                self.y -= self.speed_jump
                self.jump_times -= 1
            
    def falling(self):
        if pg.sprite.spritecollide(hitbox_d, ground_sprites, False, collided = pg.sprite.collide_mask):
            self.flashing = False
        else:
            self.y += self.speed_fall
            
    def update(self):
        if self.live:
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT] or keys[pg.K_RIGHT]:
                self.flashing = False
                if keys[pg.K_LEFT]:
                    self.movel()
                if keys[pg.K_RIGHT]:
                    self.mover()
            else:
                if self.flashing:
                    if (pg.time.get_ticks() // 100) % 2 == 0:
                        self.image = pg.transform.scale(self.image_fla, (80,80))
                    else:
                        self.image = pg.transform.scale(self.image_stop, (80,80))
                else:
                    self.image = pg.transform.scale(self.image_stop, (80,80))
            
            if keys[pg.K_UP] and self.jump_times == 0 and pg.sprite.spritecollide(hitbox_d, ground_sprites, False, collided = pg.sprite.collide_mask):
                sound_jump.play()
                self.jump_times = 9

            self.jumping()
            self.falling()
            
        else:
            if self.rect.y < 700:
                self.y += self.speed_fall
            else:
                self.restart()
                
        self.rect.center = (self.x, self.y)

class Hitbox_u(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(resource_path("image//hitbox.png")).convert()
        self.image = pg.transform.scale(self.image, (35,5))
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        
    def update(self):
        self.rect.midtop = player.rect.midtop 
        self.rect.y -= 1
    
class Hitbox_d(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(resource_path("image//hitbox.png")).convert()
        self.image = pg.transform.scale(self.image, (35,5))
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        
    def update(self):
        self.rect.midbottom = player.rect.midbottom
        self.rect.y += 1
        
class Hitbox_l(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(resource_path("image//hitbox.png")).convert()
        self.image = pg.transform.scale(self.image, (5,25))
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        
    def update(self):
        self.rect.midleft = player.rect.midleft
        self.rect.x -= 1
    
class Hitbox_r(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(resource_path("image//hitbox.png")).convert()
        self.image = pg.transform.scale(self.image, (5,25))
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        
    def update(self):
        self.rect.midright = player.rect.midright
        self.rect.x += 1
  
def clearGroups():
    for s in all_sprites:
        s.kill()
    for s in ground_sprites:
        s.kill()
    for s in fgx_sprites:
        s.kill()
    for s in fgy_sprites:
        s.kill()
    for s in enemy_sprites:
        s.kill()
    for s in hitbox_sprites:
        s.kill()

def createLevel(lv):
    def cspring(x, y, size=(100,100)):
        global spring
        spring = Spring(x, y, size)
        all_sprites.add(spring)
    def cnail(x, y, nailtype, size):
        global nail
        nail = Nail(x, y, nailtype, size)
        all_sprites.add(nail)
        enemy_sprites.add(nail)
    def cfallnail(x, y, speed):
        global fallnail
        fallnail = Fallnail(x, y, speed)
        all_sprites.add(fallnail)
        enemy_sprites.add(fallnail)
    def cenemy(x1, x2, y, speed):
        global enemy
        enemy = Enemy(x1, x2, y, speed)
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)
    def cfgx(x1, x2, y, speed):
        global fgx
        fgx = Flygroundx(x1, x2, y, speed)
        all_sprites.add(fgx)
        ground_sprites.add(fgx)
        fgx_sprites.add(fgx)
    def cfgy(x, y1, y2, speed):
        global fgy
        fgy = Flygroundy(x, y1, y2, speed)
        all_sprites.add(fgy)
        ground_sprites.add(fgy)
        fgy_sprites.add(fgy)
    
    clearGroups()
    global player, hitbox_d, hitbox_u, hitbox_l, hitbox_r
    player = Player(50,50) #待確認
    all_sprites.add(player)
    hitbox_d = Hitbox_d()
    hitbox_sprites.add(hitbox_d)
    hitbox_u = Hitbox_u()
    hitbox_sprites.add(hitbox_u)
    hitbox_l = Hitbox_l()
    hitbox_sprites.add(hitbox_l)
    hitbox_r = Hitbox_r()
    hitbox_sprites.add(hitbox_r)
    map = Map(lv)
    all_sprites.add(map)
    ground_sprites.add(map)
    
    if lv > 1:
        sound_levelup.play()
        
    if lv == 2:
        cspring(392, 530)
    elif lv == 3:
        cnail(250, 488, "n", (75,75))
        cnail(510, 488, "n", (75,75))
    elif lv == 4:
        cnail(200, 488, "n", (75,75))
        cnail(555, 495, "e", (50,50))
    elif lv== 5:
        cnail(320, 508, "n", (75,75))
        cnail(483, 38, "w", (75,75))
        cnail(483, 350, "w", (75,75))
        cspring(700,550,(70,70))
        cspring(585,380,(70,70))
    elif lv == 6:
        cnail(244, 190, "s", (75,75))
        cnail(530, 190, "s", (75,75))
        cspring(244,520)
        cspring(530,520)
        cnail(718, 340, "w", (70,70))
        cnail(718, 410, "w", (70,70))
        cnail(718, 480, "w", (70,70))
    elif lv == 7:
        cnail(308, 479, "n", (75,75))
        cnail(616, 479, "n", (75,75))
        cnail(450, 332, "s", (75,75))
        cfallnail(380,-120,16)  #speed: 16-24
        cfallnail(530,-130,20)  #speed: 16-24
    elif lv == 8:
        cnail(692, 485, "n", (70,70))
        cnail(760, 485, "n", (70,70))
        cenemy(360, 520, 470, 8)  #speed: 10-20
    elif lv == 9:
        cfgx(400,600,400,8)
        cfgy(250,600,250,12)
    elif lv == 10:
        cfgy(80,450,150,6)  #speed: 8-16
        cfgy(540,450,150,12)  #7-15
        cfgx(200,500,400,10)  #8-16
        cnail(686,310,"w",(65,65))
        cnail(686,250,"w",(65,65))
        cnail(686,190,"w",(65,65))
        cfallnail(200, -40, 16)  #16-24
        cfallnail(450, -40, 18)  #16-24
    elif lv == 11:
        cnail(539,150,"e",(70,70))
        cnail(679,295,"w",(70,70))
        cfgx(300,600,570,8)
        cfallnail(200, -20, 6)
        cfallnail(400, -20, 8)
        cfallnail(600, -20, 10)
    elif lv == 12:
        #cfallnail(200, -20, 10)
        #cfallnail(430, -20, 10)
        #cfallnail(710, -20, 10)
        cnail(195,243,"n",(75,75))
        cnail(755,495,"n",(75,75))
        cnail(453,361,"s",(65,65))
        cnail(632,500,"w",(65,65))
        cnail(453,93,"n",(70,70))
        cspring(290,277,(75,75))
        cfgx(250,350,450,8)  #10-15
        cfgy(575, 550, 310, 8)  #10-20
        cfallnail(600,-100,10)
        cfallnail(290,-200,12)
    elif lv == 13:
        cfallnail(430,-10,18)
        cfallnail(650,-100,18)
        cnail(532,175,"w",(75,75))
        cnail(377,509,"n",(75,95))
        cnail(340,260,"e",(72,72))
        cfgy(470,470,300,8)
        cfgy(700,500,280,8)
        cfgx(80,450,520,8)
        cfgx(400,500,175,8)
    elif lv == 14:
        cnail(250,30,"w",(70,70))
        cnail(123,185,"e",(70,70))
        cnail(272,175,"w",(20,20))
        cnail(760,135,"n",(67,67))
        cnail(140,463,"n",(75,65))
        cnail(220,463,"n",(75,65))
        for i in [660,730]:
            cnail(i,254,"s",(70,70))
        for i in [656,730]:
            cspring(i,485,(72,72))
        cfgy(180,600,400,7)
        cfgx(450,600,450,8)
        cfgy(470,350,100,8)
        cfallnail(410,-80,9)
        cfallnail(710,-120,8)
    elif lv == 15:
        cnail(178,87,"n",(50,50))
        cnail(358,87,"n",(50,50))
        cnail(749,30,"w",(60,60))
        cnail(586,412,"w",(53,53))
        cnail(355,230,"s",(55,55))
        cnail(406,230,"s",(55,55))
        cnail(248,225,"e",(60,85))
        cnail(113,461,"s",(50,50))
        cnail(163,461,"s",(50,50))
        cnail(393,415,"e",(40,40))
        cnail(279,415,"w",(40,40))
        for i in [670,720,770]:
            cnail(i,461,"s",(50,50))
        cspring(425, 170,(65,65))
        cspring(138,390,(60,60))
        cenemy(520,540,130,1)
        cfgx(630,750,580,6)
        cfgy(252,415,120,7)
        cfgx(420,570,390,8)
        cfgy(145,580,500,3)
        cfgy(403,580,500,7)
        #cfallnail(630,-150,14)
        cfallnail(320,-200,12)
    else:
        [print("ERROR! level not in range 1~15") if level > 1 else print("", end = "")]
        
def win():
    global playing
    playing = 2
    sound_win.play()
    clearGroups()

# 初始作業
pg.init()
pg.mixer.init()
FPS = 30
WIDTH = 800
HEIGHT  = 600

#顏色
WHITE = (255,255,255) 
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Running Square")
clock = pg.time.Clock()
level = 1 # test level
playing = 0  # 0 start, 1 playing, 2 win+end
running = True

# 角色群組
all_sprites = pg.sprite.Group()
ground_sprites = pg.sprite.Group()
fgx_sprites = pg.sprite.Group()
fgy_sprites = pg.sprite.Group()
enemy_sprites = pg.sprite.Group()
hitbox_sprites = pg.sprite.Group()

# 載入背景
bg_start = pg.image.load(resource_path("image//bg_start.png")).convert()
bg_playing = pg.image.load(resource_path("image//bg_playing.png")).convert()
bg_end = pg.image.load(resource_path("image//bg_end.png")).convert()

# 載入音樂
pg.mixer.music.load(resource_path("sound//bgm.mp3"))
pg.mixer.music.play(-1)
sound_die = pg.mixer.Sound(resource_path("sound//die.wav"))
sound_go = pg.mixer.Sound(resource_path("sound//go.wav"))
sound_jump = pg.mixer.Sound(resource_path("sound//jump.wav"))
sound_levelup = pg.mixer.Sound(resource_path("sound//levelup.wav"))
sound_win = pg.mixer.Sound(resource_path("sound//win.wav"))

# 載入字體
font = pg.font.Font(resource_path("font//TaipeiSansTCBeta-Light.ttf"), 40)

#建立start角色
button_go = Button_go(200, 100)
all_sprites.add(button_go)

while running:
    
    clock.tick(FPS)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE: #ECS to close bgm
                if pg.mixer.music.get_volume() != 0:
                    pg.mixer.music.set_volume(0)
                else:
                    pg.mixer.music.set_volume(1)
    
    # 更新畫面
    if playing == 0:
        screen.blit(bg_start, (0,0))
        
    elif playing == 1:
        
        if player.live:
            if player.x > 800:
                if level == 15:
                    win()
                else:
                    level += 1
                    createLevel(level)
            
            if pg.sprite.spritecollide(player, enemy_sprites, False, collided = pg.sprite.collide_mask) or player.y > 600:
                player.die()
                
            onfgx = pg.sprite.spritecollide(hitbox_d, fgx_sprites, False, collided = pg.sprite.collide_mask)
            if onfgx:
                for on in onfgx:                
                    player.x += on.speed * on.way
            else:    
                onfgx = pg.sprite.spritecollide(hitbox_l, fgx_sprites, False, collided = pg.sprite.collide_mask)
                if onfgx:
                    for on in onfgx:                
                        if on.way == 1:
                            player.x += on.speed * on.way
                else:            
                    onfgx = pg.sprite.spritecollide(hitbox_r, fgx_sprites, False, collided = pg.sprite.collide_mask)
                    for on in onfgx:                
                        if on.way == -1:
                            player.x += on.speed * on.way
                
            onfgy = pg.sprite.spritecollide(hitbox_d, fgy_sprites, False, collided = pg.sprite.collide_mask)
            for on in onfgy:
                player.y += on.speed * on.way               
        
        else:
            pass       
        
        hitbox_sprites.update()
        screen.blit(bg_playing, (0,0))
        
    else:
        screen.blit(bg_end, (0,0))
            
    all_sprites.update()
    all_sprites.draw(screen)
    
    if playing == 1:  #寫字
        text = font.render(f"level: {level}", True, BLACK)
        screen.blit(text, (650,10))
    
    pg.display.update()
    
    
pg.quit()    