import pygame
import pygame_gui

class Receiver():
    def __init__(self,size,title="new window"):
        pygame.init()
        self.win = pygame.display.set_mode(size)
        self.base_font = pygame.font.Font(None, 32)
        pygame.display.set_caption(title)
        self.ui_manager = pygame_gui.UIManager(size,theme_path="static/theme.json")
        self.clock = pygame.time.Clock()
        self.running = True
    def get_manager(self):
        return self.ui_manager
    #create window for input
    def receiveInput(self):
        clock = pygame.time.Clock()
        
        user_text = ''

        #create rectangle
        input_rect = pygame.Rect(350, 750, 750, 32)

        # color_active stores color(lightskyblue3) which 
        # gets active when input box is clicked by user 
        color_active = pygame.Color('black') 
  
        # color_passive store color(chartreuse4) which is 
        # color of input box. 
        color_passive = pygame.Color('gray') 
        color = color_passive 
  
        active = False
        while self.running: 
            for event in pygame.event.get(): 
  
            # if user types QUIT then the screen will close 
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    self.running = False
  
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    if input_rect.collidepoint(event.pos): 
                        active = True
                    else: 
                        active = False
  
                if event.type == pygame.KEYDOWN: 
  
                    # Check for backspace 
                    if event.key == pygame.K_BACKSPACE: 
                        # get text input from 0 to -1 i.e. end. 
                        user_text = user_text[:-1] 
  
                    # Unicode standard is used for string 
                    # formation 
                    elif event.key == pygame.K_RETURN:
                        return user_text 
                    else:
                        user_text += event.unicode
      
                    # it will set background color of screen 
            self.win.fill((255, 255, 255)) 
  
            if active: 
                color = color_active 
            else: 
                color = color_passive 
          
            # draw rectangle and argument passed which should 
            # be on screen 
            pygame.draw.rect(self.win, color, input_rect) 
  
            text_surface = self.base_font.render(user_text, True, (255, 255, 255)) 
      
            # render at position stated in arguments 
            self.win.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
      
            # set width of textfield so that text cannot get 
            # outside of user's text input 
            input_rect.w = max(100, text_surface.get_width()+10) 
            
            # display.flip() will update only a portion of the 
            # screen to updated, not full area 
            pygame.display.flip() 
      
            # clock.tick(60) means that for every second at most 
            # 60 frames should be passed. 
            clock.tick(60)

    def print_output (self, str):
        text_surface = self.base_font.render(str, True, (0, 0, 0)) 
        self.win.blit(text_surface, (0,0))

            
