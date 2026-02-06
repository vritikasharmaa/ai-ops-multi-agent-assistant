import os
import requests


def github_search(query):
    try:
        url = "https://api.github.com/search/repositories"

        headers = {
            "Accept": "application/vnd.github+json",
            "User-Agent": "ai-ops-assistant"
        }

        # Optional GitHub token (recommended)
        token = os.getenv("GITHUB_TOKEN")
        if token:
            headers["Authorization"] = f"Bearer {token}"

        params = {
            "q": query,
            "sort": "stars",
            "order": "desc"
        }

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        items = data.get("items", [])

        repos = []
        for repo in items[:3]:
            repos.append({
                "name": repo["name"],
                "stars": repo["stargazers_count"],
                "url": repo["html_url"]
            })

        return repos

    except Exception as e:
        return f"GitHub tool error: {str(e)}"
