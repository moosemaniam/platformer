"""
Todos:
1)preserve horizontal momentum
"""
import pygame,sys
G=10
FPS = 30
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,10,50)
GRN = (30,240,40)
CLR_KEY=(0,128,128)
X_OFFSET=70
Y_OFFSET=95
W=800
H=400
NUM=5
#Platform object
class platform(pygame.sprite.Sprite):
   offset=5
   count_left = 0
   count_right= 0
   score=0
   x = 0
   y = 0
   y_speed=0
   def __init__(self,left,top,width,height,color):
       pygame.sprite.Sprite.__init__(self)
       self.rect = pygame.Rect(left,top,width,height) 
       self.image= pygame.Surface((width,height)) 
       self.image.fill(color)
       self.color = color
   def draw(self,screen):
        new_rect = self.rect
        new_rect.height = new_rect.height - 5
        screen.fill(self.color,new_rect)
   
class player(pygame.sprite.Sprite):
    offset = 2
    xtarget=0
    ytarget=0
    xspeed=0
    x_change=0
    y_change=0
    screen_rect = pygame.Rect(0,0,W,H)
    platform_list=pygame.sprite.Group()
    def __init__(self,left,top,width,height,color):
       pygame.sprite.Sprite.__init__(self)
       self.rect = pygame.Rect(left,top,width,height) 
       self.image= pygame.Surface((width, height)) 
       self.image.fill(color)
       self.color = color

    def update(self):
       #Gravity 
       self.apply_gravity()
       self.rect.x += self.x_change
       #While moving left do we hit anything ?
       #While Moving right do we hit anything
       hit_list = pygame.sprite.spritecollide(self,self.platform_list,False)
       for platform in hit_list:
            if(self.x_change > 0 ):
                self.rect.right = platform.rect.left
            elif(self.x_change < 0):
                self.rect.left = platform.rect.right
      
       self.rect.y += self.y_change
       hit_list = pygame.sprite.spritecollide(self,self.platform_list,False)
       for platform in hit_list:
            if(self.y_change > 0 ):
                self.rect.bottom= platform.rect.top
            elif(self.y_change < 0):
                self.rect.top= platform.rect.bottom

            self.y_change=0
      
       #While moving up do we hit anything ?
       self.my_clamp(W,H)


    def stop(self):
        self.x_change=0
    def jump(self):
        self.rect.bottom += 2
        hit = pygame.sprite.spritecollideany(self,self.platform_list)
        self.rect.bottom -= 2
        if(hit):
            self.y_change = -2
    def left(self):
           self.x_change = -2 

    def right(self):
           self.x_change = 2 

    def my_clamp(self,W,H): 
        if(self.rect.left<=0):
            self.rect.left=0
        elif(self.rect.right>=W):
            self.rect.right = W
        if(self.rect.top <=0):
            self.rect.top = 0
        elif(self.rect.bottom >= H):
            self.rect.bottom = H
    def apply_gravity(self): 
        self.y_change +=  0.09

    def draw(self,screen):
       screen.fill(self.color,self.rect)
    
class Game(object):
      def main(self,screen):
        boundaries = []
        wsize = screen.get_width()
        hsize = screen.get_height()
        clock1 = pygame.time.Clock()
        screen.fill(BLACK)
        screen_rect = pygame.Rect(0,0,screen.get_width(),screen.get_height())
        all_Sprite_list = pygame.sprite.Group()
        player_Sprite= pygame.sprite.Group()
   #def __init__(self,left,top,width,height,color):
        joe = player(wsize/2,hsize/2,10,10,RED)
        player_Sprite.add(joe)
        ground = platform(0,hsize-10,wsize,10,GRN)
        all_Sprite_list.add(ground)
        platform_list=[]
        for i in range(1,NUM):
            platform_list.append(platform(20*i,hsize-10-20*i,20,10,WHITE))
        all_Sprite_list.add(platform_list)
        joe.platform_list=all_Sprite_list
        game_loop = True

        while (game_loop==True):
            screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if (event.type == pygame.KEYDOWN ):
                    if(event.key == pygame.K_ESCAPE):
                        return
                    if (event.key == pygame.K_RIGHT):
                       joe.right() 
                    if (event.key == pygame.K_LEFT):
                        joe.left()

                    if (event.key == pygame.K_UP):
                        joe.jump()
                if (event.type == pygame.KEYUP):
                 if event.key == pygame.K_LEFT and joe.x_change< 0: 
                    joe.stop()
                 if event.key == pygame.K_RIGHT and joe.x_change> 0:
                    joe.stop()
 

                        
            joe.update()
            all_Sprite_list.update() 
            all_Sprite_list.draw(screen) 
            joe.draw(screen) 
            pygame.display.flip()

            clock1.tick(30)












 
pygame.init()
#Create a screen
pygame.display.set_caption("Jump up")
screen = pygame.display.set_mode((W,H))
jump_up= Game()
jump_up.main(screen)
