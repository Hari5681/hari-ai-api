from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline

app = FastAPI()

# Enable CORS for your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your Firebase domain
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load a small Hugging Face model for text generation
generator = pipeline("text-generation", model="gpt2")  # lightweight, free

@app.post("/hari-ai")
async def hari_ai(req: Request):
    data = await req.json()
    message = data.get("message", "")
    task = data.get("task", "chat")  # default task = chat

    # Customize prompt based on task
    if task.lower() == "chat":
        prompt = f"User: {message}\nAI:"
    elif task.lower() == "code":
        prompt = f"Write the code for: {message}\nCode:"
    elif task.lower() == "summarize":
        prompt = f"Summarize this text: {message}\nSummary:"
    else:
        prompt = message  # fallback

    # Generate AI response
    result = generator(prompt, max_length=150, do_sample=True)
    reply = result[0]['generated_text']

    return {"reply": reply}

@app.get("/hari-ai")
def test_get():
    return {"message": "Hari AI API is running. Use POST requests."}
