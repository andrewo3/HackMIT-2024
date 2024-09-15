import pygame
pygame.init()

from receiveInput import Receiver
from llm_query import query_llm
import asyncio

async def main():
    query = Receiver((0.5,0.5),"Test")
    manager = query.get_manager()
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                query.running = False
                waiting_for_input = False
            elif event.type == pygame.KEYDOWN:
                input = query.receiveInput()
                output = query_llm(input)
                query.print_output (output)
                waiting_for_input = False
            if event.type == pygame.KEYDOWN:
                waiting_for_input = True

        await asyncio.sleep(0)
        
if __name__ == "__main__":
    asyncio.run(main())