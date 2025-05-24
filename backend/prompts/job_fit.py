__module_name__ = "job_fit"

from langchain.prompts import PromptTemplate

def get_prompt():
    return PromptTemplate(
        input_variables=["profile_data", "job_description"],
        template=(
            "Compare this LinkedIn profile data:\n\n{profile_data}\n\n"
            "With this job description:\n\n{job_description}\n\n"
            "Return a match score from 0 to 100 and highlight areas of strength and weakness."
        )
    )

# def get_prompt():
#     return (
#         "Compare this LinkedIn profile data:\n{profile_data}\n\n"
#         "with the following job description:\n{job_description}\n\n"
#         "Return a match score from 0 to 100 and specific areas where the candidate aligns well or needs improvement."
#     )
