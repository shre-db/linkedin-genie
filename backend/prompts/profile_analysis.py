__module_name__ = "profile_analysis"

from langchain.prompts import PromptTemplate

def get_prompt():
    return PromptTemplate(
        input_variables=["profile_data"],
        template=(
            "Evaluate the following LinkedIn profile data:\n\n{profile_data}\n\n"
            "Identify inconsistencies, missing sections, weak descriptions, or vague skills. "
            "Provide constructive feedback to improve each section."
        )
    )

# def get_prompt():
#     return (
#         "Evaluate the following LinkedIn profile data:\n{profile_data}\n\n"
#         "Identify inconsistencies, missing sections, weak descriptions, or vague skills. "
#         "Provide constructive feedback to improve each section."
#     )
