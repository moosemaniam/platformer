import pygame,sys
FPS = 30
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,10,50)
GRN = (30,240,40)
CLR_KEY=(0,128,128)
X_OFFSET=70
Y_OFFSET=95
W=400
H=200
NUM=10
#Platform object
class platform(pygame.sprite.Sprite):
   offset=5
   count_left = 0
   count_right= 0
   score=0
   x = 0
   y = 0
   y_speed=0
   #adsf
   def __init__(self,left,top,width,height,color):
       pygame.sprite.Sprite.__init__(self)
       self.rect = pygame.Rect(left,top,width,height) 
       self.image= pygame.Surface((width,height)) 
       self.image.fill(color)
       self.color = color
   def draw(self,screen):
        screen.fill(self.color,self.rect)
   
class player(pygame.sprite.Sprite):
    offset = 2
    xtarget=0
    ytarget=0
    xspeed=0
    yspeed=-20
    def __init__(self,left,top,width,height,color):
       pygame.sprite.Sprite.__init__(self)
       self.rect = pygame.Rect(left,top,width,height) 
       self.image= pygame.Surface((width, height)) 
       self.image.fill(color)
       self.color = color
       self.x = left
       self.y =top 
       self.xtarget = self.x
       self.ytarget = self.y

    def print_info(self):
        print "x" ,self.x
        print "y" ,self.y
        print "xtarget",self.xtarget
        print "ytarget",self.ytarget
    def update(self):
        print "update"
        if(self.xtarget>self.x):
            self.move_right()
        if(self.xtarget<self.x):
            self.move_left()
        if(self.ytarget<self.y):
            self.move_up()
        if(self.ytarget>self.y):
            self.move_down()
        if(self.yspeed==0):
            self.yspeed = -5

    def move_down(self):
       print "moving down"
       self.y = self.y + 1
       self.rect.move_ip(0,1)
    def move_up(self):
       print "moving up"
       self.y = self.y + self.yspeed 
       self.rect.move_ip(0,self.yspeed)

    def move_left(self):
       print "moving left"
       self.x = self.x - 1
       self.rect.move_ip(-1*self.offset,0)

    def move_right(self):
       print "moving right"
       self.x = self.x + 1
       self.rect.move_ip(self.offset,0)

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
        joe = player(0,hsize-15,5,5,RED)
        player_Sprite.add(joe)
        ground = platform(0,hsize-10,wsize,10,GRN)
        all_Sprite_list.add(ground)
        platform_list=[]
        for i in range(1,NUM):
            platform_list.append(platform(20*i,hsize-10-20*i,20,10,WHITE))
        all_Sprite_list.add(platform_list)
        game_loop = True


        while (game_loop==True):
            screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if ((event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                    return
                    
                if ((event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT)):
                        joe.xtarget = joe.x + 10
                if ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_LEFT)):
                        joe.xtarget = joe.x - 10

                if ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_UP)):
                        joe.ytarget = joe.y - 5 
                if ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_DOWN)):
                        joe.ytarget = joe.y + 5 

           # joe.print_info()
            joe.update()
            all_Sprite_list.update() 
            all_Sprite_list.draw(screen) 
            joe.draw(screen) 
            pygame.display.flip()

            clock1.tick(30)












 
pygame.init()
#Create a screen
w=400 
h=600
pygame.display.set_caption("Moose Pong")
screen = pygame.display.set_mode((w,h))
pygame.key.set_repeat(1000/FPS,1000/FPS)
jump_up= Game()
jump_up.main(screen)
