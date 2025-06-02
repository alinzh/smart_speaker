from smolagents import CodeAgent, OpenAIServerModel
from smolagents import DuckDuckGoSearchTool
from yandex_music_tools import music_tools
import yaml

    
with open("./conf.yaml", "r") as yamlfile:
    conf = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print("Read successful")
    

class LLMAgent:
    def __init__(self):
        search_tool = DuckDuckGoSearchTool()
        model = OpenAIServerModel(api_base=conf['api_base'], model_id=conf['model_id'], api_key=conf['openai_key'])
        self.agent = CodeAgent(tools=[search_tool] + music_tools, model=model, additional_authorized_imports=['*'])
        
    def update_memory(self):
        n_msg = len(self.agent.memory.steps)
        if n_msg > 10:
            self.agent.memory.steps = self.agent.memory.steps[n_msg-10 : -1]

    def invoke(self, user_input: str):
        self.update_memory()
        answer = self.agent.run(user_input + ' Отвечай на русском языке всегда!!!', reset=False)
        return answer