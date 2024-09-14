import pygame
UI_FONT = pygame.font.SysFont("arial",20)


class UIElem():
    def __init__(self,x,y,w,h):
        self.x,self.y,self.w,self.h = (x,y,w,h)
    def update(self,window):
        window_size = window.get_size()
        self.scaled_rect = pygame.Rect(int(self.x*window_size[0]),
                                       int(self.y*window_size[1]),
                                       int(self.w*window_size[0]),
                                       int(self.h*window_size[1]))
        
class Button(UIElem):
    def __init__(self,x,y,w,h,text,fill,border,thickness,radius):
        super().__init__(x,y,w,h)
        self.x,self.y,self.w,self.h = (x,y,w,h)
        self.fill = fill
        self.border = border
        self.text = text
        self.scaled_rect = None
        self.radius = radius
        self.thickness = thickness
        self.text_surf = UI_FONT.render(self.text,True,self.border)
    def update(self,window,events):
        super().update(window)
        window_size = window.get_size()
        self.scaled_rect = pygame.Rect(int(self.x*window_size[0]),
                                       int(self.y*window_size[1]),
                                       int(self.w*window_size[0]),
                                       int(self.h*window_size[1]))
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.scaled_rect.collidepoint(*event.pos):
                    print("Clicked",self.text)
    def draw(self,window: pygame.Surface):
        pygame.draw.rect(window,self.fill,self.scaled_rect,border_radius=self.radius)
        pygame.draw.rect(window,self.border,self.scaled_rect,width=self.thickness,border_radius=self.radius)
        center = (self.scaled_rect.x+(self.scaled_rect.w-self.text_surf.get_width())//2,
                  self.scaled_rect.y+(self.scaled_rect.h-self.text_surf.get_height())//2)
        window.blit(self.text_surf,center)
        
        
class Note():
    def __init__(self,start,end,key):
        self.start = start
        self.end = end
        self.key = key

class ScaleBar(UIElem):
    def __init__(self,x,y,w,h):
        super().__init__(x,y,w,h)
        self.bg_color = (60,60,60)
        self.clicked = False
        self.scale = [1,1]
        self.drag_strength = 0.03
    def update(self,window,events):
        super().update(window)
        buttons = pygame.mouse.get_pressed(num_buttons=3)
        motion = pygame.mouse.get_rel()
        if buttons[0] and self.clicked:
            self.scale[0]+=motion[0]*self.drag_strength
            self.scale[1]+=motion[1]*self.drag_strength
            if self.scale[0]<1:
                self.scale[0] = 1
            if self.scale[1]<1:
                self.scale[1] = 1
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==1 and self.scaled_rect.collidepoint(pygame.mouse.get_pos()):
                    self.clicked = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 2:
                    self.clicked = False
    def draw(self,window):
        surf = pygame.Surface(self.scaled_rect.size)
        surf.fill(self.bg_color)
        pygame.draw.line(surf,(0,0,0),(self.scaled_rect.w//2,0),(self.scaled_rect.w//2,self.scaled_rect.h))
        pygame.draw.line(surf,(0,0,0),(0,self.scaled_rect.h//2),(self.scaled_rect.w,self.scaled_rect.h//2))
        window.blit(surf,self.scaled_rect.topleft)
  
class PianoRoll(UIElem):
    def __init__(self,x,y,w,h):
        super().__init__(x,y,w,h)
        self.bg_color = (60,60,60)
        self.pos = [0,0] # num beats over from 0, and num keys down from top
        self.notes = []
        self.scale = [20,10] #pixels per grid piece
        self.surface = None
        self.scroll_strength = 0.2
        self.scale_bar = ScaleBar(0.9,0.1,0.02,0.02)
        
    def update(self,window,events):
        super().update(window)
        self.scale_bar.update(window,events)
        self.scale = [20*self.scale_bar.scale[0],10*self.scale_bar.scale[1]]
        self.surface = pygame.Surface(self.scaled_rect.size)
        for event in events:
            if event.type == pygame.MOUSEWHEEL:
                #print(event.x,event.y,mouse_buttons)
                self.pos[0]+=self.scroll_strength*-event.x
                if self.pos[0]<0:
                    self.pos[0] = 0
                self.pos[1]+=self.scroll_strength*-event.y
                if self.pos[1]<0:
                    self.pos[1] = 0
                elif self.pos[1]>87:
                    self.pos[1] = 87
            
    def draw(self,window):
        offsetx = -self.scale[0]*(self.pos[0]%1)
        offsety = self.scale[1]*(self.pos[1]%1)
        c = offsetx+self.scale[0]
        self.surface.fill(self.bg_color)
        while c<self.scaled_rect.w: #draw vertical grid lines
            pygame.draw.line(self.surface,(255,255,255),(c,0),(c,self.scaled_rect.h))
            c+=self.scale[0]
        
        c = offsety-self.scale[1]
        start_note = int(self.pos[1])
        while c<self.scaled_rect.h:
            pygame.draw.line(self.surface,(255,255,255),(0,c),(self.scaled_rect.w,c))
            black_key = start_note%12 in [1,4,6,9,11]
            pygame.draw.rect(window,(0,0,0) if black_key else (255,255,255),pygame.Rect(0,c+self.scaled_rect.top,self.scaled_rect.left,self.scale[1]))
            start_note+=1
            c+=self.scale[1]
        
        print(start_note)
        c = offsety-self.scale[1]
        
        
        window.blit(self.surface,(self.scaled_rect.x,self.scaled_rect.y))
        self.scale_bar.draw(window)