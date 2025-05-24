__module_name__ = "career_guidance"

from langchain.prompts import PromptTemplate

def get_prompt():
    return PromptTemplate(
        input_variables=["profile_data", "target_role"],
        template=(
            "Given this LinkedIn profile data:\n{profile_data}\n\n"
            "And the user's desired role: {target_role}, analyze the career alignment. "
            "Suggest any missing skills, certifications, or experience needed, and recommend learning resources."
        )
    )

# def get_prompt():
#     return (
#         "Given this profile data: \n{profile_data}\n\n"
#         "and the user's desired role: {target_role},"
#         "analyze career alignment and recommend skills or learning paths to bridge any gaps."
#     )