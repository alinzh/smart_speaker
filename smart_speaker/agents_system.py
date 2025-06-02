from utils import clean_music_dir, run_track
from agents import LLMAgent

agent = LLMAgent()

def main(query: str):
    clean_music_dir()
    res = agent.invoke(query)
    print(res)
    
    suc = run_track()
    if suc:
        print('Track successfully played!')
        
if __name__ == "__main__":
    while True:
        inp = input()
        main(inp)
    
    
    