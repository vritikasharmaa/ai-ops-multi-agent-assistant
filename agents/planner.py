import re

def create_plan(task: str):
    task = task.strip().lower()

    # WEATHER TASK
    if "weather" in task or "temperature" in task:
        match = re.search(r"(in|at|for)\s+([a-zA-Z\s]+)", task)

        city = match.group(2).strip().title() if match else "Delhi"

        return {
            "steps": [
                {
                    "tool": "weather",
                    "city": city
                }
            ]
        }

    # GITHUB TASK
    if "github" in task or "repo" in task:
        return {
            "steps": [
                {
                    "tool": "github_search",
                    "query": task
                }
            ]
        }

    return {"steps": []}
