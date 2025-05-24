__module_name__ = "langgraph_graph"

"""
A simple sequential graph

[START]
   ↓
Profile Analyzer
   ↓
Content Rewriter
   ↓
Job Fit Evaluator
   ↓
Career Guide
   ↓
[END]
"""

from langgraph.graph import StateGraph, END, Graph
from .state_schema import ProfileBotState
from .handlers import analyze_node, rewrite_node, job_fit_node, guide_node
from backend.memory import get_memory_saver


def build_graph():
    """
    Builds the LangGraph workflow with all nodes.
    Returns an uncompiled graph object.
    """
    graph = StateGraph(ProfileBotState)

    graph.add_node("AnalyzeProfile", analyze_node)
    graph.add_node("RewriteContent", rewrite_node)
    graph.add_node("EvaluateJobFit", job_fit_node)
    graph.add_node("CareerGuidance", guide_node)

    graph.set_entry_point("AnalyzeProfile")

    graph.add_edge("AnalyzeProfile", "RewriteContent")
    graph.add_edge("RewriteContent", "EvaluateJobFit")
    graph.add_edge("EvaluateJobFit", "CareerGuidance")
    graph.add_edge("CareerGuidance", END)

    return graph


# def get_graph_runner() -> Graph:
#     """
#     Compiles the graph and plugs in persistent memory for automatic checkpointing.
#     """
#     raw_graph = build_graph()
#     memory = get_memory_saver()
#     return raw_graph.compile(checkpointer=memory)

def get_graph_runner() -> Graph:
    raw_graph = build_graph()
    print("[langgraph_graph.py] Calling get_memory_saver()...")
    memory_instance = get_memory_saver()
    print(f"[langgraph_graph.py] Object received from get_memory_saver(): {memory_instance}")
    print(f"[langgraph_graph.py] Type of object received: {type(memory_instance)}")

    if not hasattr(memory_instance, 'get_next_version'):
        print(f"[langgraph_graph.py] ERROR: Checkpointer (type {type(memory_instance)}) from get_memory_saver() LACKS get_next_version method BEFORE compile!")
    else:
        print(f"[langgraph_graph.py] Checkpointer (type {type(memory_instance)}) from get_memory_saver() HAS get_next_version method BEFORE compile.")

    return raw_graph.compile(checkpointer=memory_instance)
