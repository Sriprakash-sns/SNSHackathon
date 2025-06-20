# AgentPM Web App

This is a full-stack web application simulating an Agentic AI Product Manager using React (frontend) and FastAPI (backend).

---

## 🧰 Tech Stack

- **Frontend**: React + Vite + TailwindCSS
- **Backend**: FastAPI (Python 3.10+)
- **Agents**: Modular AI agents for PM tasks
- **LLM**: OpenAI GPT-4o (via API)
- **Storage**: PostgreSQL, FAISS (for vector search)
- **Orchestration**: CrewAI (planned for end-to-end agent flow)
- **Deployment**: Docker + Docker Compose

---

## 📦 Project Structure

```
project-root/
├── backend/
│   └── app/
│       ├── shared_utils/            # Shared logic across agents
│       ├── agents/
│       │   ├── talent_acquisition/
│       │   │   ├── __init__.py
│       │   │   ├── agent.py
│       │   │   ├── utils.py
│       │   │   └── prompts.py
│       │   ├── roadmap_planning/
│       │   │   ├── __init__.py
│       │   │   ├── agent.py
│       │   │   ├── utils.py
│       │   │   └── prompts.py
│       │   ├── progress_monitoring/
│       │   │   ├── __init__.py
│       │   │   ├── agent.py
│       │   │   ├── utils.py
│       │   │   └── prompts.py
│       │   ├── gtm_strategy/
│       │   │   ├── __init__.py
│       │   │   ├── agent.py
│       │   │   ├── utils.py
│       │   │   └── prompts.py
│       │   ├── sales_feedback/
│       │   │   ├── __init__.py
│       │   │   ├── agent.py
│       │   │   ├── utils.py
│       │   │   └── prompts.py
│       ├── orchestration/
│       │   └── orchestrator.py           # CrewAI orchestration entrypoint
│       ├── tests/
│       │   ├── conftest.py              # Shared test fixtures and mocks
│       │   ├── test_talent.py
│       │   ├── test_roadmap.py
│       │   ├── test_progress.py
│       │   ├── test_gtm.py
│       │   └── test_feedback.py
│       └── mock_data/
│           ├── resumes.json
│           ├── jd_sample.txt
│           ├── feedback.csv
│           ├── features.json
│           ├── reviews.json
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   ├── components/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── TalentAgent.jsx
│   │   │   ├── RoadmapAgent.jsx
│   │   │   ├── ProgressAgent.jsx
│   │   │   ├── GTMAgent.jsx
│   │   │   └── FeedbackAgent.jsx
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Talent.jsx
│   │   │   ├── Roadmap.jsx
│   │   │   ├── Progress.jsx
│   │   │   ├── GTM.jsx
│   │   │   └── Feedback.jsx
│   │   ├── api/
│   │   │   ├── axios.js
│   │   │   └── apiClient.js            # Centralized client with interceptors
│   │   │   └── axios.js
│   │   └── styles/
│   │       └── index.css
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── index.html
│   └── package.json
├── docker-compose.yml
├── README.md
```

...

## 🧠 AI + Orchestration

Agents are currently modular and a unified orchestration runtime is scaffolded under `orchestration/orchestrator.py`.

### CrewAI Integration (Planned)
We will use **CrewAI** to coordinate:
- Task routing across agents
- Multi-agent memory and tool use
- Dynamic delegation and follow-ups

This will simulate real-world Product Manager workflows from hiring to post-launch feedback.

### Sample Orchestrator Template (WIP)
```python
# backend/app/orchestration/orchestrator.py
try:
    from crewai import Crew, Task, Agent
except ImportError:
    raise ImportError("Please install crewai to run orchestration: pip install crewai")

import json

# Load agent definitions from config (example: JSON file or Python dict)
with open('backend/app/orchestration/agent_config.json', 'r') as f:
    agent_data = json.load(f)

def create_agent(entry):
    return Agent(name=entry['name'], goal=entry['goal'])

def create_task(agent, description):
    return Task(agent=agent, description=description)

# Build agents and tasks from config
agents = [create_agent(a) for a in agent_data['agents']]
tasks = [create_task(agents[i], t) for i, t in enumerate(agent_data['tasks'])]

# Initialize the crew
pm_crew = Crew(agents=agents, tasks=tasks)

# Run the orchestration
if __name__ == '__main__':
    pm_crew.kickoff()
```
if __name__ == '__main__':
    pm_crew.kickoff()
```

...
