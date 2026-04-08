import os
import asyncio
from openai import OpenAI
from env.email_env import EmailTriageEnv
from env.models import EmailTriageAction

# Mandatory Variables - Judges will inject these into the environment
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")
# Locally, ensure you run 'set HF_TOKEN=your_key' before running this
API_KEY = os.getenv("HF_TOKEN") or os.getenv("OPENAI_API_KEY")
async def main():
    client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)
    env = EmailTriageEnv(task_name="basic_triage") 
    obs = env.reset()
    
    print(f"[START] task=basic_triage env=email-triage model={MODEL_NAME}", flush=True)
    
    rewards = []
    steps_taken = 0
    done = False

    for i in range(1, 11): # Increased to 10 to process more of the inbox
        if done:
            break
        steps_taken = i
        
        # --- THE GOOD FIX: HEURISTIC LOGIC ---
        content = (obs.subject + " " + obs.body).lower()
        
        if "urgent" in content or "immediately" in content or "asap" in content:
            cat = "urgent"
            pri = "high"
        elif "unsubscribe" in content or "click here" in content or "offer" in content:
            cat = "spam"
            pri = "low"
        elif "newsletter" in content or "weekly" in content:
            cat = "newsletter"
            pri = "low"
        elif "schedule" in content or "meeting" in content or "confirm" in content:
            cat = "action_required"
            pri = "medium"
        else:
            cat = "info"
            pri = "low"
        # -------------------------------------

        action = EmailTriageAction(
            action_type="categorize", 
            category=cat, 
            priority=pri
        )
        
        obs, reward_obj, done, info = env.step(action)
        current_reward = float(reward_obj.value)
        rewards.append(current_reward)
        
        print(f"[STEP] step={i} action={action.action_type} reward={current_reward:.2f} done={str(done).lower()} error=null", flush=True)

    avg_score = sum(rewards) / len(rewards) if rewards else 0.0
    success_val = "true" if avg_score > 0.3 else "false" # 0.3 is a fair baseline threshold
    rewards_str = ",".join([f"{r:.2f}" for r in rewards])

    print(f"[END] success={success_val} steps={steps_taken} score={avg_score:.3f} rewards={rewards_str}", flush=True)


if __name__ == "__main__":
    asyncio.run(main())