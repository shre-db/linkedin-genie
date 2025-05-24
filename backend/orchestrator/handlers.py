__module_name__ = "handlers"

from .state_schema import ProfileBotState
from agents.career_guide import CareerGuideAgent
from agents.content_rewriter import ContentRewriterAgent
from agents.job_fit_evaluator import JobFitEvaluatorAgent
from agents.profile_analyzer import ProfileAnalyzerAgent

# Intialize Agents
analyzer = ProfileAnalyzerAgent()
rewriter = ContentRewriterAgent()
evaluator = JobFitEvaluatorAgent()
guide = CareerGuideAgent()

# Define node callables
def analyze_node(state: ProfileBotState) -> ProfileBotState:
    result = analyzer.analyze(state.linkedin_data)
    state.profile_analysis = result
    state.steps_completed["analyzed"] = True
    return state

def rewrite_node(state: ProfileBotState) -> ProfileBotState:
    rewrites = {}
    for section_name, content in state.linkedin_data.items():
        rewrites[section_name] = rewriter.rewrite(
            section_name, content, state.target_role
        )
    state.content_rewrites = rewrites
    state.steps_completed["rewritten"] = True
    return state

def job_fit_node(state: ProfileBotState) -> ProfileBotState:
    result = evaluator.evaluate_fit(state.linkedin_data, state.job_description)
    state.job_fit_report = result
    state.steps_completed["job_fit_completed"] = True
    return state

def guide_node(state: ProfileBotState) -> ProfileBotState:
    result = guide.guide(state.linkedin_data, state.target_role)
    state.career_guidance = result
    state.steps_completed["career_guided"] = True
    return state   
