# 🤖 AI-Powered Code Reviewer CLI with CrewAI + OpenAI + GitHub

This project is a smart, modular AI-based code reviewer designed to analyze GitHub repositories and pull requests using [CrewAI](https://docs.crewai.com), OpenAI embeddings, and classification logic. It retrieves code, identifies essential files, analyzes code quality and functionality, and provides concise, intelligent suggestions using agents.

---

## 🚀 Features

✅ Analyze **entire branches or specific pull requests**  
✅ Auto-detect **default branches** (`main`, `develop`, etc.)  
✅ Identify **essential files** using OpenAI embeddings  
✅ Check for:
- ❌ Missing imports/exports
- 🧠 Dead code & cyclic dependencies
- 🔁 React hook misuse (`useEffect`, `useState`, etc.)
- ⚠️ Broken routes, incorrect logic  
✅ Review only the **relevant files**, ignoring boilerplate  
✅ Generate concise suggestions (≤ 10 lines) via AI agents  
✅ Output review results in `.txt` and `.json` formats

---

## 🗂️ Folder Structure

```
crewAI_project/
│
├── cli/                  # CLI entry point
│   └── main.py
│
├── github/               # GitHub interaction logic
│   ├── branch_utils.py
│   └── repo_utils.py
│
├── embeddings/           # AI classification logic
│   └── classifier.py
│
├── crews/                # CrewAI agents setup
│   └── crew_setup.py
│
├── tasks/                # AI task generation
│   └── task_factory.py
│
├── validator/            # Review post-processing
│   └── review_parser.py
│
├── utils/                # Constants & helpers
│   └── constants.py
└── .env                  # API keys & environment vars
```

---

## ⚙️ Setup Instructions

1. **Clone this repo**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Create a `.env` file**

```env
OPENAI_API_KEY=your-openai-key
GITHUB_TOKEN=your-github-token
```

4. **Run CLI tool**

- For analyzing a branch:

```bash
python cli/main.py
```

- For analyzing a PR (example for PR #5):

```python
# Inside main.py, call:
fetch_pull_request_files("username/repo", 5)
```

---

## 🧠 Technologies Used

- [CrewAI](https://docs.crewai.com) – AI agent framework
- [OpenAI](https://platform.openai.com) – Embeddings & GPT-based review logic
- [GitHub API](https://docs.github.com/en/rest) – Repo & PR file fetching
- Python 3.10+

---

## 📌 Notes

- Supports **branch-based** and **PR-based** review.
- Auto-generates `.txt` and `.json` output in root directory.
- Avoids boilerplate using extension and folder filters.

---



---

## 💡 Future Improvements

- [ ] Add UI interface (Streamlit or React)
- [ ] Integrate automatic PR commenting
- [ ] Allow review config via CLI args

---

## 📬 Contact

Have questions or suggestions?  
Feel free to open an [issue](https://github.com/your-username/your-repo/issues) or message me directly.

---

**Give this project a ⭐ if you like AI + DevTools integration!**
