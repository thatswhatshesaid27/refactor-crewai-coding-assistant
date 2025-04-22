import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv  
from github.repo_utils import fetch_repo_files, fetch_file_content_from_branch
from github.branch_utils import get_default_branch
from embeddings.classifier import ai_classification
from crews.crew_setup import setup_crew
from tasks.task_factory import create_tasks
from validator.review_parser import convert_txt_to_json
from crewai import Crew
from utils.constants import ESSENTIAL_EXTENSIONS, IGNORE_DIRS, IGNORE_FILES
load_dotenv()
repo_name = "thatswhatshesaid27/Personal-Portfolio-HTML-CSS-only"
branch = get_default_branch(repo_name, "develop")
files = fetch_repo_files(repo_name, branch)
agents = setup_crew()

classified_files = ai_classification(files, repo_name, branch)
selected_files = [path for path, score in classified_files if score >= 60]

with open("pr_review_results.txt", "a", encoding="utf-8") as result_file:
    for file_path in selected_files:
        ext = os.path.splitext(file_path)[1]
        if ext not in ESSENTIAL_EXTENSIONS or any(ignored in file_path for ignored in IGNORE_DIRS) or os.path.basename(file_path) in IGNORE_FILES:
            continue

        file_content = fetch_file_content_from_branch(repo_name, file_path, branch)
        if not file_content.strip():
            continue

        tasks = create_tasks(
            file_path,
            file_content,
            "Personal Portfolio created using HTML and CSS with only layout and design without any functionality and logic and no backend",
            agents
        )

        crew = Crew(agents=agents, tasks=tasks)
        results = crew.kickoff()
        results_text = results.results if hasattr(results, "results") else str(results)

        result_file.write(f"Review results for {file_path} (from branch {branch})\n")
        result_file.write(f"{results_text.strip()}\n")
        result_file.write("##########################################################\n\n")

print("\u2705 Text output saved to 'pr_review_results.txt'")
convert_txt_to_json()
