import pygame
pygame.init()

from receiveInput import Receiver
from llm_query import query_llm
import asyncio

async def main():
    win = Receiver((0.5,0.5),"Test")
    manager = win.get_manager()

    while win.running:
        input = win.receiveInput()
        output = query_llm (input)
        print(output)
        await asyncio.sleep(0)
        
if __name__ == "__main__":
    asyncio.run(main())