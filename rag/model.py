from openai import OpenAI
from config.settings import Settings

class OpenRouterLLM:
    def __init__(self, config: Settings):
        self.config = config
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=config.openrouter_api_key
        )
    
    def generate(self, prompt: str) -> str:
        model = self.config.openrouter_model
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content