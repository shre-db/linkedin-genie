__module_name__ = "career_guide"

from backend.llm import get_chat_model
from backend.prompts.career_guidance import get_prompt

class CareerGuideAgent:
    def __init__(self):
        self.model = get_chat_model()
        self.prompt_template = get_prompt()

    def guide(self, profile_data: dict, target_role: str) -> str:
        prompt = self.prompt_template.format(profile_data=profile_data, target_role=target_role)
        response = self.model.invoke(prompt)
        return response