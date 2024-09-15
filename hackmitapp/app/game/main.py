import pygame
pygame.init()

from window import Window
from llm_query import query_llm
from ui import *
import asyncio

# usage: query_llm(input_string) returns output_str the answer to the query
#sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    
async def main():
    #reader, writer = await asyncio.open_connection('127.0.0.1',1236)
    #request = "testing\n"
    #writer.write(request.encode("utf-8"))
    #await writer.drain()
    #print("sent")
    #response = await reader.read(1024)
    #print(response.decode('utf-8'))
    win = Window((0.5,0.5),"Test")
    #test_button = Button(0.1,0.1,0.3,0.3,"Testing",(30,30,30),(100,255,0),5,10)
    piano_roll = PianoRoll(0.1,0.1,0.8,0.8)
    waiting_for_input = True
    while win.running:
        events = pygame.event.get()
        #test_button.update(win.win,events)
        piano_roll.update(win.win,events)
        if win.update(events):
            #test_button.draw(win.win)
            piano_roll.draw(win.win)
            win.draw()
        
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    win.running = False
                    waiting_for_input = False
                elif event.type == pygame.KEYDOWN:
                    input = win.receiveInput()
                    output = query_llm(input)
                    win.print_output (output)
                    waiting_for_input = False
                if event.type == pygame.KEYDOWN:
                    waiting_for_input = True
                    break
        await asyncio.sleep(0)
    
if __name__ == "__main__":
    asyncio.run(main())
    