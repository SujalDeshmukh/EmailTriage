from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
# Inside server/app.py
from env.email_env import EmailTriageEnv
from env.models import EmailTriageAction
import uvicorn

app = FastAPI(title="Email Triage OpenEnv")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

_env: EmailTriageEnv = None

@app.post("/reset")
def reset(task: str = Query(default="basic_triage")):
    global _env
    _env = EmailTriageEnv(task_name=task)
    obs = _env.reset()
    return {"observation": obs.dict(), "done": False}

@app.post("/step")
def step(action: EmailTriageAction):
    obs, reward, done, info = _env.step(action)
    return {
        "observation": obs.dict(),
        "reward": reward.dict(),
        "done": done,
        "info": {"steps_taken": len(info["history"])}
    }

@app.get("/state")
def state():
    return _env.state().dict()

@app.get("/health")
def health():
    return {"status": "ok"}


# ... your existing FastAPI code (app = FastAPI...)

def main():
    """Entry point for the OpenEnv validator and CLI."""
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()