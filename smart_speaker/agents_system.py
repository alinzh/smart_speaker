from utils import clean_music_dir, run_track, speech_to_text, text_to_speech
from agents import LLMAgent
import time
import pygame
from prompt import system_prompt


agent = LLMAgent()

def main(query: str):
    pygame.quit()
    clean_music_dir()
    agent.agent.system_prompt = system_prompt
    res = agent.invoke(query)
    text_to_speech(res)
    suc = run_track("./output.mp3", early_stop=False)
    time.sleep(3)
    suc = run_track("./music_data/current.mp3")
    if suc:
        print('Track successfully played!')
        
    return res
        
        
if __name__ == "__main__":
    inp = speech_to_text()
    while True:
        inp = input()
        main(inp)
    
    
    