import uuid
import streamlit as st
from app.config import APP_TITLE, APP_DESCRIPTION
from app.ui_utils import show_footer
from app.ui_utils import run_profile_analysis

# Page setup
st.set_page_config(page_title=APP_TITLE, layout="centered")

# Title and description
st.title(APP_TITLE)
st.markdown(APP_DESCRIPTION)

# User Inputs
st.subheader("🔗 Enter LinkedIn Profile URL")
linkedin_url = st.text_input("Paste your public LinkedIn profile URL here")
print(f"LinkedIn URL in the main module: {linkedin_url}")

st.subheader("🎯 Target Job Role")
job_role = st.text_input("What job role are you aiming for? (e.g., Data Scientist, Product Manager)")

# Analyze button
analyze_button = st.button("🚀 Analyze My Profile")

user_id = str(uuid.uuid4())

# Placeholder for output
if analyze_button:
    if not linkedin_url or not job_role:
        st.warning("Please provide both a LinkedIn URL and a target job role.")
    else:
        with st.spinner("Analyzing your profile... Please wait."):
            state = run_profile_analysis(linkedin_url, job_role, user_id)

            st.success("✅ Analysis Complete!")

            print(f"Final Output: {state}")

            # st.subheader("📊 Profile Analysis Summary")
            # st.write(state.analysis_result)

            # st.subheader("✍️ Rewritten Sections")
            # st.write(state.rewritten_content)

            # st.subheader("📌 Job Fit Report")
            # st.write(state.job_fit_score)
            # st.write(state.job_fit_feedback)

            # st.subheader("🎓 Career Guidance")
            # st.write(state.career_recommendation)

# Footer
show_footer()
