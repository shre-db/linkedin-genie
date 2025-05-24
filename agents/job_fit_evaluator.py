__module_name__ = "job_fit_evaluator"

from backend.llm import get_chat_model
from backend.prompts.job_fit import get_prompt

class JobFitEvaluatorAgent:
    def __init__(self):
        self.model = get_chat_model()
        self.prompt_template = get_prompt()

    def evaluate_fit(self, profile_data: dict, job_description: str) -> dict:
        prompt = self.prompt_template.format(
            profile_data=profile_data,
            job_description=job_description
        )
        return self.model.invoke(prompt)

        # return {
        #     "raw_response": response
        # }
