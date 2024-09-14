from window import Window
import asyncio
import pygame
from pygame_gui.elements import *
from llm_query import query_llm
# usage: query_llm(input_string) returns output_str the answer to the query

async def main():
    win = Window(0.5,0.5,"Test")
    manager = win.get_manager()
    hello_button = UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                             text='Say Hello',
                                             manager=manager)
    while win.running:
        win.draw()
        win.update()
        await asyncio.sleep(0)
    
if __name__ == "__main__":
    asyncio.run(main())