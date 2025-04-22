import openai
from github.repo_utils import fetch_file_content_from_branch
from utils.constants import ESSENTIAL_EXTENSIONS

def ai_classification(files, repo_name, branch='main'):
    file_scores = {}
    for file in files:
        path = file.get("path") or file.get("filename")
        if path.endswith(tuple(ESSENTIAL_EXTENSIONS)):
            content = fetch_file_content_from_branch(repo_name, path, branch)
            if not content:
                continue
            embedding = openai.embeddings.create(
                model="text-embedding-ada-002",
                input=[content]
            ).data[0].embedding
            score = sum(embedding)
            file_scores[path] = score

    if not file_scores:
        return []

    min_score, max_score = min(file_scores.values()), max(file_scores.values())
    normalized_scores = {
        path: ((score - min_score) / (max_score - min_score)) * 100 if min_score != max_score else 50.0
        for path, score in file_scores.items()
    }

    return sorted(normalized_scores.items(), key=lambda x: x[1], reverse=True)
