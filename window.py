import pygame
import pygame_gui

class Window():
    def __init__(self,w,h,title="new window"):
        pygame.init()
        desktop = (pygame.display.Info().current_w,pygame.display.Info().current_h)
        scaled_desktop = (int(desktop[0]*w),int(desktop[1]*h))
        self.win = pygame.display.set_mode(scaled_desktop)
        pygame.display.set_caption(title)
        self.ui_manager = pygame_gui.UIManager(scaled_desktop,theme_path="static/theme.json")
        self.clock = pygame.time.Clock()
        self.running = True
    def get_manager(self):
        return self.ui_manager
    def update(self):
        tick = self.clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False
            self.ui_manager.process_events(event)
        self.ui_manager.update(tick/1000)
    def draw(self):
        self.ui_manager.draw_ui(self.win)
        pygame.display.update()
        self.win.fill((0,0,0))