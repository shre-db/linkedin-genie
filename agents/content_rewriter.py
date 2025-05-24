__module_name__ = "content_rewriter"

from backend.llm import get_chat_model
from backend.prompts.content_rewriting import get_prompt

class ContentRewriterAgent:
    def __init__(self):
        self.model = get_chat_model()
        self.prompt_template = get_prompt()

    def rewrite(self, section_name: str, current_content: str, target_role: str = None) -> str:
        prompt = self.prompt_template.format(
            section_name=section_name,
            current_content=current_content,
            target_role=target_role or "the same role"
        )
        return self.model.invoke(prompt)
    
