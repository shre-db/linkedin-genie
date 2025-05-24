__module_name__ = "content_rewriting"

from langchain.prompts import PromptTemplate

def get_prompt():
    return PromptTemplate(
        input_variables=["section_name", "current_content", "target_role"],
        template=(
            "Rewrite the '{section_name}' section of a LinkedIn profile to better align with the target role: {target_role}.\n\n"
            "Current content:\n{current_content}\n\n"
            "Improved version:"
        )
    )

# def get_prompt():
#     return (
#         "Rewrite the following LinkedIn '{section_name} section to better align with the industry best practices "
#         "and the target role '{target_role}':\n\n"
#         "Current content:\n{current_content}\n\n"
#         "Improved version:"
#     )