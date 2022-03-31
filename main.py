import pygame,sys
pygame.init()


Screen = pygame.display.set_mode((700,700))
BG = (80,100,200)




###################Images#######################
Europe = pygame.image.load("Europe.png")





while 1:
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
  
  Screen.display(Europe,(0,0))
  pygame.display.update()
  
  