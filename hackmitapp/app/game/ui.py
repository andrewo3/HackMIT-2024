import pygame
from llm_query import query_llm
from time import sleep
import fluidsynth

pygame.init()
fs = fluidsynth.Synth()
fs.start()
sfid = fs.sfload("piano.sf2")
fs.program_select(0,sfid,0,0)
UI_FONT = pygame.font.SysFont("arial",10)
NOTE_NAMES = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]

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
                if event.button == 1:
                    self.clicked = False
    def draw(self,window):
        surf = pygame.Surface(self.scaled_rect.size)
        surf.fill(self.bg_color)
        pygame.draw.line(surf,(0,0,0),(self.scaled_rect.w//2,0),(self.scaled_rect.w//2,self.scaled_rect.h))
        pygame.draw.line(surf,(0,0,0),(0,self.scaled_rect.h//2),(self.scaled_rect.w,self.scaled_rect.h//2))
        window.blit(surf,self.scaled_rect.topleft)
  
def note_name(num):
    return NOTE_NAMES[num%12]+str((num+9)//12)
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
        self.drag = False
        self.drag_note = 0
        self.drag_start = 0
        self.playing = False
        
    def update(self,window,events):
        super().update(window)
        self.scale_bar.update(window,events)
        self.scale = [20*self.scale_bar.scale[0],10*self.scale_bar.scale[1]]
        self.surface = pygame.Surface(self.scaled_rect.size)
        if self.playing:
            self.pos[0]+=0.1
            for note in self.notes:
                notex = int((note.start-self.pos[0])*self.scale[0])
                notex_end = int((note.end-self.pos[0])*self.scale[0])
                if int(notex)==0:
                    fs.noteon(0,note.key+9,100)
                elif int(notex_end)==0:
                    fs.noteoff(0,note.key+9)
                    
        for event in events:
            if event.type == pygame.MOUSEWHEEL:
                #print(event.x,event.y,mouse_buttons)
                self.pos[0]+=self.scroll_strength*event.x
                if self.pos[0]<0:
                    self.pos[0] = 0
                self.pos[1]+=self.scroll_strength*event.y
                if self.pos[1]<0:
                    self.pos[1] = 0
                elif self.pos[1]>87:
                    self.pos[1] = 87
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.playing += 1
                    self.playing %= 2
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.scaled_rect.collidepoint(pygame.mouse.get_pos()):
                    num_notes = (event.pos[1]-self.scaled_rect.top)//self.scale[1]
                    dist_from_left = (event.pos[0]-self.scaled_rect.left)/self.scale[0]
                    self.drag_note = int(self.pos[1])+35-num_notes
                    self.drag_start = int(self.pos[0]+dist_from_left)
                    self.drag = True
                elif event.button == 3:
                    offsety = self.scale[1]*(self.pos[1]%1)
                    remove = None
                    for note in self.notes:
                        notey = (int(self.pos[1]+35-note.key))*self.scale[1]+offsety
                        notex = (note.start-self.pos[0])*self.scale[0]
                        if -self.scale[1]<notey<self.scaled_rect.h:
                            note_rect = pygame.Rect(notex+self.scaled_rect.left,notey+self.scaled_rect.top,self.scale[0]*(note.end-note.start+1),self.scale[1])
                            print(note_rect)
                            if note_rect.collidepoint(pygame.mouse.get_pos()):
                                remove = note
                    if remove is not None:
                        self.notes.remove(remove)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and self.drag and self.scaled_rect.collidepoint(pygame.mouse.get_pos()):
                    dist_from_left = (event.pos[0]-self.scaled_rect.left)/self.scale[0]
                    drag_end = int(self.pos[0]+dist_from_left)
                    print(event.pos,note_name(int(self.drag_note)),drag_end-self.drag_start+1)
                    new_note = Note(self.drag_start,drag_end,int(self.drag_note))
                    if not (self.drag_start,drag_end,int(self.drag_note)) in [(n.start,n.end,n.key) for n in self.notes]:
                        for note in self.notes:
                            overlap = new_note.start <= note.start and new_note.end >= note.start or \
                                note.start <= new_note.start and note.end >= new_note.start
                            if note.key == new_note.key and overlap:
                                break 
                        else:
                            self.notes.append(new_note)
                    self.drag = False

    def draw(self,window):
        offsetx = -self.scale[0]*(self.pos[0]%1)
        offsety = self.scale[1]*(self.pos[1]%1)
        c = offsetx+self.scale[0]
        self.surface.fill(self.bg_color)
        for note in self.notes:
            notey = (int(self.pos[1]+35-note.key))*self.scale[1]+offsety
            notex = (note.start-self.pos[0])*self.scale[0]
            if -self.scale[1]<notey<self.scaled_rect.h:
                pygame.draw.rect(self.surface,(0,128,255),pygame.Rect(notex,notey,self.scale[0]*(note.end-note.start+1),self.scale[1]),border_radius=40)
                pygame.draw.rect(self.surface,(255,255,255),pygame.Rect(notex,notey,self.scale[0]*(note.end-note.start+1),self.scale[1]),width=1,border_radius=40)
                #print(notey)
        while c<self.scaled_rect.w: #draw vertical grid lines
            pygame.draw.line(self.surface,(255,255,255),(c,0),(c,self.scaled_rect.h))
            c+=self.scale[0]
        
        c = offsety-self.scale[1]
        start_note = int(self.pos[1])
        
        while c<self.scaled_rect.h: #draw horizontal grid lines and note names
            pygame.draw.line(self.surface,(255,255,255),(0,c),(self.scaled_rect.w,c))
            black_key = start_note%12 in [1,4,6,9,11]
            pygame.draw.rect(window,(0,0,0) if black_key else (255,255,255),pygame.Rect(0,c+self.scaled_rect.top,self.scaled_rect.left,self.scale[1]))
            note_name = UI_FONT.render(NOTE_NAMES[start_note%12]+str((start_note+45)//12),True,(255,255,255) if black_key else (0,0,0))
            window.blit(note_name,(self.scaled_rect.left-note_name.get_width(),c+self.scaled_rect.top+(self.scale[1]-note_name.get_height())//2))
            start_note-=1
            c+=self.scale[1]
        pygame.draw.rect(window,(0,0,0),pygame.Rect(0,0,self.scaled_rect.left,self.scaled_rect.top))
        pygame.draw.rect(window,(0,0,0),pygame.Rect(0,window.get_height()-self.scaled_rect.top,self.scaled_rect.left,self.scaled_rect.top))
            
        
        
        #print(start_note)
        c = offsety-self.scale[1]
        
        
        window.blit(self.surface,(self.scaled_rect.x,self.scaled_rect.y))
        self.scale_bar.draw(window)

class TextBox(UIElem):
    def __init__(self,x,y,w,h):
        super().__init__(x,y,w,h)
        self.active = False
        self.color_active = pygame.Color('black') 
        self.color_passive = pygame.Color('gray') 
        self.color = self.color_passive
        self.input_rect = pygame.Rect(self.x, self.y, 500, 30)
        self.user_text = ''
        self.output = ''
    def update(self,window,events):
        super().update(window)
        
        self.active = False
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit() 
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                    if self.input_rect.collidepoint(event.pos): 
                        self.active = True
                    else: 
                        self.active = False
            elif event.type == pygame.KEYDOWN: 
  
                    # Check for backspace 
                    if event.key == pygame.K_BACKSPACE: 
                        # get text input from 0 to -1 i.e. end. 
                        self.user_text = self.user_text[:-1] 
  
                    # Unicode standard is used for string 
                    # formation 
                    elif event.key == pygame.K_RETURN:
                        self.output = query_llm(self.user_text)
                    else:
                        self.user_text += event.unicode
            if self.active: 
                self.color = self.color_active 
            else: 
                self.color = self.color_passive
    def draw(self,window):
        pygame.draw.rect(window, self.color, self.input_rect, 2, 3) 
  
        text_surface = UI_FONT.render(self.user_text, True, (255, 255, 255)) 
      
            # render at position stated in arguments 
        window.blit(text_surface, (self.input_rect.x+5, self.input_rect.y+5)) 
      
            # set width of textfield so that text cannot get 
            # outside of user's text input 
        self.input_rect.w = max(100, text_surface.get_width()+10) 
        self.print_output(self.output, window)
        
            # display.flip() will update only a portion of the 
            # screen to updated, not full area 
        #pygame.display.flip() 
      
            # clock.tick(60) means that for every second at most 
            # 60 frames should be passed. 
        #self.clock.tick(60)
    def print_output (self, str, window):
        text_surface = UI_FONT.render(str, True, (255, 255, 255)) 
        window.blit(text_surface, (self.scaled_rect.x+self.scaled_rect.w+10, 9*self.h/10))

