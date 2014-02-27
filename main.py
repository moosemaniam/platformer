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
    def __init__(self,left,top,width,height,color):
       pygame.sprite.Sprite.__init__(self)
       self.rect = pygame.Rect(left,top,width,height) 
       self.image= pygame.Surface((width, height)) 
       self.image.fill(color)
       self.color = color
       self.x = left
       self.y =top 
    def update(self):
        pass

    def move_left(self):
       self.x = self.x - 1
       self.rect.move_ip(-1*self.offset,0)

    def move_right(self):
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
                    joe.move_right()
                if ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_LEFT)):
                    joe.move_left()
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
pygame.key.set_repeat(10,10)
jump_up= Game()
jump_up.main(screen)
