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
class platform(object):
   offset=5
   count_left = 0
   count_right= 0
   score=0
   def __init__(self,left,top,width,height,color):
       self.Rect = pygame.Rect(left,top,width,height) 
       self.color = color
   def draw(self,screen):
        screen.fill(self.color,self.Rect)
   
class player(platform):
    pass
class Game(object):
      def main(self,screen):
        boundaries = []
        wsize = screen.get_width()
        hsize = screen.get_height()
        clock1 = pygame.time.Clock()
        screen.fill(BLACK)
        screen_rect = pygame.Rect(0,0,screen.get_width(),screen.get_height())

   #def __init__(self,left,top,width,height,color):
        joe = player(0,hsize-20,5,10,RED)
        ground = platform(0,hsize-10,wsize,10,GRN)
        platform_list=[]
        for i in range(1,NUM):
            platform_list.append(platform(20*i,hsize-10-20*i,20,10,WHITE))
        game_loop = True

        while (game_loop==True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if ((event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                    return
                    """
                if ((event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT)):
                    bat1.move_right()
                if ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_LEFT)):
                    bat1.move_left()
                if ((event.type == pygame.KEYDOWN and event.key == pygame.K_s)):
                    bat2.move_right()
                if ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_a)):
                    bat2.move_left()
                    """
            ground.draw(screen)
            joe.draw(screen)
            for pltfrm in platform_list:
                pltfrm.draw(screen)
            pygame.display.flip()

            clock1.tick(30)












 
pygame.init()
#Create a screen
w=400 
h=600
pygame.display.set_caption("Moose Pong")
screen = pygame.display.set_mode((w,h))
pygame.key.set_repeat(5,100)
jump_up= Game()
jump_up.main(screen)
