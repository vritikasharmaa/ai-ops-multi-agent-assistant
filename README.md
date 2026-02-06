🤖 AI Ops Multi-Agent Assistant

An AI-powered multi-agent system that plans, executes, and verifies DevOps-style tasks using LLMs and real-world APIs.

This project demonstrates a **Planner → Executor → Verifier** agent architecture and produces a complete end-to-end working result.

---

 🚀 Setup Instructions (Run Locally)
 1️⃣ Clone the Repository
```bash
git clone https://github.com/vritikasharmaa/ai-ops-multi-agent-assistant.git
cd ai-ops-multi-agent-assistant
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Set Environment Variables
Create a .env file using .env.example as reference.

5️⃣ Run the Application
streamlit run main.py
The app will be available at:
👉 http://localhost:8501

🔐 Environment Variables (.env.example)
OPENAI_API_KEY=your_openai_api_key_here
WEATHER_API_KEY=your_openweathermap_api_key_here
GITHUB_TOKEN=optional_github_token
.env is ignored using .gitignore to keep secrets safe.

🧠 Architecture Overview
🔹 Agents
Planner Agent
Converts user input into a structured JSON execution plan using an LLM

Executor Agent
Executes the plan by calling relevant tools (APIs)

Verifier Agent
Validates execution results and checks for failures

🔧 Tools
Weather Tool
Fetches real-time weather using OpenWeatherMap API

GitHub Search Tool
Searches top GitHub repositories using GitHub Search API

🔌 Integrated APIs
OpenAI API – for planning and structured outputs

OpenWeatherMap API – for real-time weather data

GitHub REST API – for repository search

🧪 Example Prompts to Test
Check weather in Mumbai

Check weather in Bengaluru

Check weather in New York

Check weather in Delhi

Search GitHub for DevOps automation scripts

⚠️ Known Limitations & Tradeoffs
Planner accuracy depends on LLM output quality

Limited to predefined tools (weather, GitHub search)

No persistent memory between runs

Rate limits may apply for external APIs
