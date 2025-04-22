import requests
import os

GITHUB_API = "https://api.github.com/repos/"
HEADERS = {"Authorization": os.getenv("GITHUB_TOKEN")}

def get_default_branch(repo_name, user_branch=None):
    if user_branch:
        return user_branch
    url = f"{GITHUB_API}{repo_name}"
    response = requests.get(url, headers=HEADERS)
    return response.json().get("default_branch", "main") if response.status_code == 200 else "main"
