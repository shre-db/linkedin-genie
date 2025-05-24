import ollama

# import subprocess
# import json

# OLLAMA_MODEL = "gemma3:1b"

# def generate_response(prompt, model=OLLAMA_MODEL, options=None):
#     """
#     Generate a response from the specified Ollama model.

#     Args:
#         prompt (str): The input prompt to send to the model.
#         model (str): The model name/tag to use.
#         options (dict): Additional options for Ollama (optional).

#     Returns:
#         str: The generated response from the model.
#     """
#     cmd = [
#         "ollama",
#         "run",
#         model,
#         prompt
#     ]
#     if options:
#         # Ollama CLI does not support options directly, but you can extend this if needed
#         pass

#     try:
#         result = subprocess.run(cmd, capture_output=True, text=True, check=True)
#         return result.stdout.strip()
#     except subprocess.CalledProcessError as e:
#         print(f"Error running Ollama: {e.stderr}")
#         return None

# if __name__ == "__main__":
#     prompt = "Hello, how can I help you today?"
#     response = generate_response(prompt)
#     print("Ollama response:", response)

OLLAMA_MODEL = "gemma3:1b"

def generate_response_ollama_pkg(prompt, model=OLLAMA_MODEL, options=None):
    """
    Generate a response from the specified Ollama model using the ollama Python package.

    Args:
        prompt (str): The input prompt to send to the model.
        model (str): The model name/tag to use.
        options (dict): Additional options for Ollama (optional).

    Returns:
        str: The generated response from the model.
    """
    try:
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            options=options or {}
        )
        return response['message']['content'].strip()
    except Exception as e:
        print(f"Error using ollama package: {e}")
        return None

if __name__ == "__main__":
    prompt = "Does gemma3-1B model through Ollama require a GPU? Can it run purely on a high performance CPU with 32 GB RAM?"
    response = generate_response_ollama_pkg(prompt)
    print("Ollama package response:", response)