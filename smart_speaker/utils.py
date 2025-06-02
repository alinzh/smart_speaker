import shutil, os
import pygame, time

def clean_music_dir():
    path = "./music_data"
    for item in os.listdir(path):
        try: shutil.rmtree(p) if os.path.isdir(p:=os.path.join(path, item)) else os.remove(p)
        except: pass
        
def run_track():
    if os.path.exists("./music_data/current.mp3"):
        pygame.init()
        pygame.mixer.init(frequency=44100, buffer=1024)
        sound = pygame.mixer.Sound("./music_data/current.mp3")
        sound.play()
        time.sleep(5)
        pygame.quit()
        return True
    else:
        return False