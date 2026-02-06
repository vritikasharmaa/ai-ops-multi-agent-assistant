from tools.github_tool import github_search
from tools.weather_tool import get_weather


def execute_plan(plan_json):

    results = []
    logs = []

    logs.append("Executor started execution")

    steps = plan_json.get("steps", [])

    for i, step in enumerate(steps):

        tool = step.get("tool")
        logs.append(f"Running step {i + 1} using tool: {tool}")

        try:
            if tool == "github_search":
                query = step.get("query")
                result = github_search(query)

            elif tool == "weather":
                city = step.get("city")
                result = get_weather(city)

            else:
                result = f"Unsupported tool: {tool}"

        except Exception as e:
            result = f"Error executing {tool}: {str(e)}"

        results.append({
            "tool": tool,
            "result": result
        })

    logs.append("Execution completed")

    return results, logs
