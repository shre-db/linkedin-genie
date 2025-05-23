from backend.llm import get_chat_model

def test_chat_model_response():
    chat_model = get_chat_model()
    result = chat_model.predict("What is one tip to improve a LinkedIn headline?")
    assert result and isinstance(result, str)
    print(result)