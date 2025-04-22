import json
import re

def convert_txt_to_json(txt_file="pr_review_results.txt", json_file="pr_review_results.json"):
    results = []
    with open(txt_file, "r", encoding="utf-8") as file:
        content = file.read()

    blocks = content.split("##########################################################")
    for block in blocks:
        if not block.strip():
            continue

        lines = block.strip().splitlines()
        header = lines[0]
        body = "\n".join(lines[1:])

        if "Review results for" in header:
            try:
                file_path = header.split("Review results for")[1].split("(from")[0].strip()
            except:
                continue

            code_blocks = []
            code_block_pattern = re.compile(r"```(\w*)\n(.*?)```", re.DOTALL)
            matches = code_block_pattern.findall(body)
            for lang, code in matches:
                code_blocks.append({
                    "language": lang or "text",
                    "code": code.strip()
                })

            explanation = code_block_pattern.sub("", body).strip()
            issues = re.findall(r"^\s*(?:\d+\.\s+|\*\s+|\-\s+)(.+)$", explanation, re.MULTILINE)

            results.append({
                "file_path": file_path,
                "explanation": explanation.split("\n\n")[0].strip(),
                "issues_detected": issues,
            })

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)

    print(f"\u2705 Enhanced JSON saved to {json_file}")
