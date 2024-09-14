import pygame
#import pygame_gui

class Window():
    def __init__(self,mon_scale,title="new window"):
        display_size = (pygame.display.Info().current_w,pygame.display.Info().current_h)
        final_size = (int(display_size[0]*mon_scale[0]),int(display_size[1]*mon_scale[1]))
        self.win = pygame.display.set_mode(final_size)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True
    def update(self,events):
        tick = self.clock.tick(60)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False
        return self.running
    def draw(self):
        pygame.display.update()
        self.win.fill((0,0,0))