#!/usr/bin/env python3

import threading as tr
from SpeechPython.speech import Speech
import time


# import sys
# import select
# import termios
import pygame as pg
import subprocess
from pygame.locals import *


endGame = False 

class RosFaceTR(tr.Thread):
    def __init__(self):
        super(RosFaceTR, self).__init__()

    def run(self):
        pass
        
class AsyncTalker(tr.Thread):
    def __init__(self):
        super(AsyncTalker, self).__init__()
    
    def initSentence(self, sentence, talkId):
        self.sentence = sentence
        self.talkId = talkId
  
    def run(self):
        global s;
        s.create_talk(self.sentence, self.talkId)       
        s.play_talk(self.talkId) 

def main():
    time.sleep(2)
    # Start the game
    global endGame
    global s
    s = Speech()
    talk = AsyncTalker()
    talk.initSentence("Welcome to the emotion game.", "id1")
    tr1 = RosFaceTR().start()
    talk.run()
 
    talk.initSentence("Do you want to play the game?", "id2")
    talk.run()

    if 'y' in s.listen(3):
        endGame = False
    else: 
        talk.initSentence("Oh, Maybe next time.", "id3")
        talk.run()   
        endGame = True
    
    while not endGame:
        for event in pg.event.get(): 
            if event.type == QUIT:
                endGame = True
        pressedKey = pg.key.get_pressed()
        #if pressedKey[K_q]
        #    endGame = True
    

pg.init()    
main()

    

    
    


