import pygame

def main():
  pygame.init()
  pygame.display.set_caption("PyGame Tutorial")
  screen = pygame.display.set_mode((800,600))
  running = True
  while running:
    for event in pygame.event.get():
      key=pygame.key.get_pressed()
      if key[pygame.K_ESCAPE]:
        running = False;

main()
