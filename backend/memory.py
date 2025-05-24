import os
import atexit
from dotenv import load_dotenv
from contextlib import ExitStack # Keep ExitStack if you intend to use it for other resources later

from langgraph.checkpoint.base import BaseCheckpointSaver
from langgraph.checkpoint.memory import InMemorySaver
from backend.orchestrator.state_schema import ProfileBotState # Assuming this path is correct
import inspect # Not used in the provided code, can be removed if not needed elsewhere

load_dotenv()

# Global state
# _stack = ExitStack() # You likely don't need this global ExitStack for InMemorySaver
_saver: BaseCheckpointSaver | None = None

# Register a cleanup function to ensure the ExitStack is closed if it were used.
# This part might become unnecessary if you remove the global _stack.
# If you keep the global _stack for other future resources, then keep this.
# atexit.register(_stack.close)

def get_memory_saver() -> BaseCheckpointSaver:
    """
    Lazily initializes an InMemorySaver.
    """
    global _saver
    if _saver is None:
        # Directly instantiate InMemorySaver.
        # It does NOT need to be wrapped in an ExitStack.
        _saver = InMemorySaver()
        # print(f"[memory.py] Initialized InMemorySaver. Type: {type(_saver)}") # For debugging
    return _saver


def save_state(user_id: str, state: ProfileBotState):
    saver = get_memory_saver()
    # LangGraph's InMemorySaver.put expects the state to be a dictionary or a JSON-serializable object.
    # profile_bot_state is a Pydantic model, so .model_dump() is correct here.
    saver.put(user_id, state.model_dump())

def load_state(user_id: str) -> ProfileBotState:
    saver = get_memory_saver()
    saved_data = saver.get(user_id)
    # The 'get' method returns a dictionary or None.
    # If None, return a new ProfileBotState. Otherwise, unpack the dictionary.
    return ProfileBotState(**saved_data) if saved_data else ProfileBotState(user_id=user_id)