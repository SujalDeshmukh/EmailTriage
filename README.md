# Email Triage OpenEnv (v2026)

---
title: Email Triage OpenEnv
emoji: 📧
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false
---

## 📋 Project Overview
**Email Triage OpenEnv** is a high-fidelity reinforcement learning (RL) environment designed to simulate a corporate workplace inbox. Built for the **OpenEnv 2026 Hackathon**, this environment evaluates AI agents on their ability to manage complex communication workflows, prioritize tasks under **SLA pressure**, and handle **bilingual (Hindi-English)** content.

---

## 📂 File Architecture & Functions

| File / Folder | Role & Description |
| :--- | :--- |
| **`env/email_env.py`** | **The Core Engine.** Manages the environment lifecycle, task loading, and state transitions. |
| **`env/models.py`** | **Data Schemas.** Contains Pydantic models for `EmailTriageObservation` and `EmailTriageAction` to ensure strict type safety. |
| **`env/graders.py`** | **The Referee.** Logic to score agent actions based on category accuracy, priority routing, and professional reply quality. |
| **`server/app.py`** | **Production Gateway.** A FastAPI server that exposes the environment as a web service for remote evaluation on Hugging Face Spaces. |
| **`inference.py`** | **The Agent.** A baseline implementation using LLMs (Qwen-2.5-72B) to solve the environment's tasks. |
| **`Dockerfile`** | **Infrastructure.** Instructions to containerize the environment for cloud deployment. |
| **`pyproject.toml`** | **Manifest.** Lists all Python dependencies and project metadata. |
| **`openenv.yaml`** | **Validator Config.** Required metadata for the OpenEnv automated grading system. |

---

## 🎯 Tasks Performed
The environment consists of three primary tasks designed to test different agent capabilities:

1. **`basic_triage` (Easy)**
   - **Scenario:** High-volume inbox with clear spam and internal notifications.
   - **Test:** Can the agent accurately differentiate between noise and signal?

2. **`priority_routing` (Medium)**
   - **Scenario:** Emails with misleading or vague subject lines.
   - **Test:** Can the agent parse the body text to identify high-priority issues that "look" low priority at first glance?

3. **`full_inbox_management` (Hard)**
   - **Scenario:** Complex, multi-turn threads involving bilingual (Hinglish) content and customer complaints.
   - **Test:** Can the agent write professional replies and manage **SLA decay** (rewards decrease as time passes)?

---

## 🚀 Execution Guide

### 1. Local Setup
Ensure you are in the project root directory and install the environment in editable mode:
```bash
pip install -e .
