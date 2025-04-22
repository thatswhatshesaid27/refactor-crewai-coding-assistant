import requests
import base64

# Set these
owner = "thatswhatshesaid27"
repo = "Personal-Portfolio-HTML-CSS-only"
pull_number = 6
GITHUB_TOKEN = "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"  # Replace with your token

# Headers
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Step 1: Get PR info (to extract head branch name)
pr_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}"
pr_resp = requests.get(pr_url, headers=headers)
pr_data = pr_resp.json()

head_branch = pr_data["head"]["ref"]
print(f"🔍 PR is from branch: {head_branch}")


# print('runing this before file url')

# Step 2: Get files changed in PR
files_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/files"

print('runing this after file url')
files_resp = requests.get(files_url, headers=headers)
# print('files_resp', files_resp)
changed_files = files_resp.json()
# print('changed files', changed_files)

# Step 3: Fetch and print content of each file from head branch
for file in changed_files:
    path = file["filename"]
    print(f"\n📄 File: {path}")

    content_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={head_branch}"
    content_resp = requests.get(content_url, headers=headers)

    if content_resp.status_code == 200:
        content_json = content_resp.json()
        encoded = content_json.get("content", "")
        decoded = base64.b64decode(encoded).decode("utf-8")
        print(decoded)
    else:
        print(f"⚠️ Could not fetch {path}: {content_resp.status_code}")
