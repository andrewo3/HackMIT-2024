from receiveInput import Receiver
import pygame
from pygame_gui.elements import *
from llm_query import query_llm

def main():
    win = Receiver((800,800),"Test")
    manager = win.get_manager()

    while True:
        input = win.receiveInput()
        win.print_output (query_llm (input))
        
if __name__ == "__main__":
    main()