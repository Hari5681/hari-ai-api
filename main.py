from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow your frontend (Firebase) to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with your Firebase domain for security
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/hari-ai")
async def hari_ai(req: Request):
    data = await req.json()
    user_id = data.get("user_id")
    message = data.get("message")
    task = data.get("task")
    
    # Dummy response for testing
    reply = f"Task: {task}, Message: {message}"
    return {"reply": reply}

@app.get("/hari-ai")
def test_get():
    return {"message": "Hari AI API is running. Use POST requests."}
