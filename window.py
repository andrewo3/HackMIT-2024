import pygame
import pygame_gui

class Window():
    def __init__(self,size,title="new window"):
        pygame.init()
        self.win = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.ui_manager = pygame_gui.UIManager(size,theme_path="static/theme.json")
        self.clock = pygame.time.Clock()
        self.running = True
    def get_manager(self):
        return self.ui_manager
    def update(self,*ui_elements):
        tick = self.clock.tick(60)
        self.ui_manager.update(tick/1000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                for elem in ui_elements:
                    if event.ui_element == elem:
                        print(elem,"pressed.")
            self.ui_manager.process_events(event)
    def draw(self):
        self.ui_manager.draw_ui(self.win)
        pygame.display.update()
        self.win.fill((0,0,0))