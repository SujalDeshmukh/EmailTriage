import os
import uvicorn
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

# Import your local environment modules
from env.email_env import EmailTriageEnv
from env.models import EmailTriageAction

# REPLACE 'Sujal12334' with your actual Hugging Face username if it's different
# This root_path is CRITICAL for Hugging Face Spaces to map routes correctly.
app = FastAPI(
    title="Email Triage OpenEnv",
    root_path="/Sujal12334/email-triage-env"
)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_methods=["*"], 
    allow_headers=["*"]
)

# Global environment instance
_env: EmailTriageEnv = None

@app.get("/", include_in_schema=False)
async def root():
    """Redirects the main Space URL to the API documentation."""
    return RedirectResponse(url="/docs")

@app.post("/reset")
def reset(task: str = Query(default="basic_triage")):
    global _env
    _env = EmailTriageEnv(task_name=task)
    obs = _env.reset()
    # obs.dict() ensures Pydantic models are serialized to JSON
    return {"observation": obs.dict(), "done": False}

@app.post("/step")
def step(action: EmailTriageAction):
    global _env
    if _env is None:
        return {"error": "Environment not initialized. Call /reset first."}
    
    obs, reward, done, info = _env.step(action)
    return {
        "observation": obs.dict(),
        "reward": reward.dict(),
        "done": done,
        "info": {"steps_taken": len(info.get("history", []))}
    }

@app.get("/state")
def state():
    if _env is None:
        return {"error": "No active environment state."}
    return _env.state().dict()

@app.get("/health")
def health():
    return {"status": "ok"}

def main():
    """Entry point for Hugging Face Spaces."""
    # Port must be 7860 for Hugging Face
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
