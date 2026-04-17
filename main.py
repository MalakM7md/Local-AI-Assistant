import gradio as gr
import requests
from fastapi import FastAPI

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_text(prompt):
    if not prompt:
        return "Please enter a prompt."

    data = {
        "model": "qwen:0.5b",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=data)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        return f"Error: {str(e)}"

interface = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=4, placeholder="Ask something..."),
    outputs="text",
    title="My Local AI Assistant",
    description="Running qwen:0.5b locally with Ollama"
)

app = FastAPI()
app = gr.mount_gradio_app(app, interface, path="/")