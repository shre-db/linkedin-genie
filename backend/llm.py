__module_name__ = "llm"

from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain_community.chat_models.huggingface import ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "mistralai/Mixtral-8x7B-Instruct-v0.1")
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

def get_chat_model(temperature: float = 0.1):
    llm = HuggingFaceEndpoint(
        repo_id=MODEL_NAME,
        temperature=temperature,
        huggingfacehub_api_token=HF_API_TOKEN,
        stop_sequences=["\nObservation:", "Observation:", "</s>"]
    )
    return ChatHuggingFace(llm=llm)
