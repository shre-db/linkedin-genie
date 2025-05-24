import streamlit as st
from backend.orchestrator.langgraph_graph import get_graph_runner
from backend.orchestrator.state_schema import ProfileBotState

def show_footer():
    st.markdown("---")
    st.markdown("Built with ❤️ for LearnTube.ai | [GitHub](https://github.com/shre-db/linkedin-genie)")

def get_mock_profile():
    return {
        "name": "Jane Doe",
        "about": "Aspiring data scientist with strong foundations in ML and Python.",
        "experience": [
            {"title": "Data Analyst", "company": "Acme Corp", "description": "Worked on dashboards and reporting."}
        ],
        "skills": ["Python", "SQL", "Data Visualization"]
    }

def run_profile_analysis(linkedin_url: str, job_role: str, user_id: str):
    print(f"LinkedIn URL Inside run_profile_analysis function: {linkedin_url}")
    profile_data = get_mock_profile()

    # Build initial state
    initial_state = {
        "linkedin_data": profile_data,
        "target_role": job_role,
        # "profile_data": profile_data,
        "chat_history": [],
        "session_id": user_id,
    }

    graph = get_graph_runner()

    print(f"initial_state: {initial_state['linkedin_data']}")

    # Run graph with persistent memory
    final_state: ProfileBotState = graph.invoke(
        initial_state,
        config={"configurable": {"thread_id": user_id}},
    )

    return final_state
