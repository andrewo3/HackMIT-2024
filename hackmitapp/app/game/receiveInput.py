import pygame
import pygame_gui

class Receiver():
    def __init__(self,size,title="new window"):
        pygame.init()
        self.win = pygame.display.set_mode(size)
        self.window_width = self.win.get_size()[0]
        self.window_height = self.win.get_size()[1]
        font_size = self.window_width // 20
        self.base_font = pygame.font.SysFont(None, 32)
        pygame.display.set_caption(title)
        self.ui_manager = pygame_gui.UIManager(size,theme_path="static/theme.json")
        self.clock = pygame.time.Clock()
        self.running = True
        self.textAlignLeft = 0
        self.textAlignRight = 1
        self.textAlignCenter = 2
        self.textAlignBlock = 3
    def get_manager(self):
        return self.ui_manager
    

    def drawText(self,surface, text, color, rect, font, align=0, aa=False, bkg=None):
        lineSpacing = -2
        spaceWidth, fontHeight = font.size(" ")[0], font.size("Tg")[1]

        listOfWords = text.split(" ")
        if bkg:
            imageList = [font.render(word, 1, color, bkg) for word in listOfWords]
            for image in imageList: image.set_colorkey(bkg)
        else:
            imageList = [font.render(word, aa, color) for word in listOfWords]

        maxLen = rect[2]
        lineLenList = [0]
        lineList = [[]]
        for image in imageList:
            width = image.get_width()
            lineLen = lineLenList[-1] + len(lineList[-1]) * spaceWidth + width
            if len(lineList[-1]) == 0 or lineLen <= maxLen:
                lineLenList[-1] += width
                lineList[-1].append(image)
            else:
                lineLenList.append(width)
                lineList.append([image])

        lineBottom = rect[1]
        lastLine = 0
        for lineLen, lineImages in zip(lineLenList, lineList):
            lineLeft = rect[0]
            if align == self.textAlignRight:
                lineLeft += + rect[2] - lineLen - spaceWidth * (len(lineImages)-1)
            elif align == self.textAlignCenter:
                lineLeft += (rect[2] - lineLen - spaceWidth * (len(lineImages)-1)) // 2
            elif align == self.textAlignBlock and len(lineImages) > 1:
                spaceWidth = (rect[2] - lineLen) // (len(lineImages)-1)
            if lineBottom + fontHeight > rect[1] + rect[3]:
                break
            lastLine += 1
            for i, image in enumerate(lineImages):
                x, y = lineLeft + i*spaceWidth, lineBottom
                surface.blit(image, (round(x), y))
                lineLeft += image.get_width() 
            lineBottom += fontHeight + lineSpacing

        if lastLine < len(lineList):
            drawWords = sum([len(lineList[i]) for i in range(lastLine)])
            remainingText = ""
            for text in listOfWords[drawWords:]: remainingText += text + " "
            return remainingText
        return ""

    #create window for input
    def receiveInput(self):     
        user_text = ''
        #create rectangle
        input_rect = pygame.Rect(self.window_width / 4, 4*self.window_height / 6, 1000, 30)

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
            pygame.draw.rect(self.win, color, input_rect, 2, 3) 
  
            text_surface = self.base_font.render(user_text, True, (0, 0, 0)) 
      
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
            self.clock.tick(60)

    def print_output (self, str):
        text_surface = self.base_font.render(str, True, (0, 0, 0)) 
        self.drawText(self.win, str, (0, 0, 0), self.base_font, self.textAlignBlock, True)
        self.win.blit(text_surface, (self.window_width / 4, 7*self.window_height / 8))
        pygame.display.flip()

            
