import pygame
#initialising pygame and its functions 
pygame.init()
# creating game window and title
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Draw Rectangle")
# Display game window 
background_image = pygame.image.load("bg2.jpg").convert()
#.blit() is how you copy the contents of one screen to another.
screen.blit(background_image,[0,0])


#Color or rectangle
BLUE=(0,0,255)
Blue_rect=player=pygame.Rect(200,200,30,30)
#Draw Rectangle of blue color [left, top, width, height]

pygame.draw.rect(screen,BLUE,Blue_rect)

#Draw WHITE Rectangle on given coordinates
WHITE=(255,255,255)
enemy=pygame.Rect(100,100,30,30)
pygame.draw.rect(screen,WHITE,enemy)



#Update the screen after pasting rectangle on it
pygame.display.update()
