import base64
import requests
import os

GITHUB_API = "https://api.github.com/repos/"
HEADERS = {"Authorization": os.getenv("GITHUB_TOKEN")}

def fetch_repo_files(repo_name, branch):
    branch_url = f"{GITHUB_API}{repo_name}/branches/{branch}"
    branch_response = requests.get(branch_url, headers=HEADERS)
    if branch_response.status_code != 200:
        raise Exception("Failed to fetch branch details")

    commit_sha = branch_response.json().get("commit", {}).get("sha")
    if not commit_sha:
        raise Exception("Commit SHA not found for branch")

    tree_url = f"{GITHUB_API}{repo_name}/git/trees/{commit_sha}?recursive=1"
    tree_response = requests.get(tree_url, headers=HEADERS)
    if tree_response.status_code != 200:
        raise Exception("Failed to fetch repository file list")

    return tree_response.json().get("tree", [])

def fetch_file_content_from_branch(repo_name, file_path, branch):
    url = f"{GITHUB_API}{repo_name}/contents/{file_path}?ref={branch}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return base64.b64decode(response.json().get("content", "")).decode('utf-8')
    return ""
