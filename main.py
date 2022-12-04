import pygame
import random
pygame.init()
import time 
height = 600
width = 800
screen  = pygame.display.set_mode((width , height))

class Visualiser:
    def __init__(self):
        self.lines_height = {}
    
    def draw_lines(self):
        for i in range(width//10):
            self.lines_height[i] = random.randint(100,400)
        return self.lines_height
    
    def sorting(self,i):

            first = self.lines_height[i]
            second = self.lines_height[i+1]
            if first < second:
                self.lines_height[i],self.lines_height[i+1] = self.lines_height[i+1],self.lines_height[i]
            return (self.lines_height[i+1],i )
            



        
        
max_range = width//10
given_value = 0  
bubble = Visualiser()



j, m = None, None 
run = True
clock = pygame.time.Clock
while run:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                c = bubble.draw_lines()
                j = True
            if event.key == pygame.K_s:
                m = True

    if j:
        for i in c.keys():
            pygame.draw.line(screen, (250,250,250),(5+i*10, c[i]),(5+i*10,600))



    if m :
        if given_value == max_range - 1:
            given_value = 0
            max_range -= 1


        b = bubble.sorting(given_value)
        pygame.draw.line(screen,(100,100,0),(5+b[1]*10,b[0]),(5+b[1]*10,600))
        time.sleep(0.003)
        given_value += 1
    
    if max_range == 1 :
        for i in bubble.lines_height.keys():
            pygame.draw.line(screen, (250,250,250),(5+i*10, c[i]),(5+i*10,600))
            m = None



    pygame.display.flip()