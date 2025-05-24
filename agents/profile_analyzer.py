__module_name__ = "profile_analyzer"

from backend.llm import get_chat_model
from backend.prompts.profile_analysis import get_prompt

class ProfileAnalyzerAgent:
    def __init__(self):
        self.model = get_chat_model()
        self.prompt_template = get_prompt()

    def analyze(self, profile_data: dict) -> str:
        prompt = self.prompt_template.format(profile_data=profile_data)
        return self.model.invoke(prompt)