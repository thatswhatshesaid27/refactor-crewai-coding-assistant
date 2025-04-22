from crewai import Task

def create_tasks(file_name, file_content, functionality_description, agents):
    ext = file_name.split('.')[-1].upper()
    
    task_1 = Task(
        description=f"Quick syntax check for {ext} file:\n\n{file_content}...",  # Limit content preview
        instruction=(
        "You must NOT provide large code blocks. "
        "Only suggest fixes where needed, using no more than 10 lines of code total. "
        "Avoid full rewrites or non-critical suggestions."
    ),
        agent=agents[0],
        expected_output=(
            "• Identify 3–6 syntax/formatting issues.\n"
            "• Only describe critical issues briefly (1-2 lines each).\n"
            "• Do not rewrite full code blocks.\n"
            "• Only include small code suggestions (max 10 lines total) and only if necessary."
        )
    )
    
    task_2 = Task(
        description=f"Brief security & performance review for {ext} file:\n\n{file_content}...", 
            instruction=(
            "You must NOT provide large code blocks. "
            "Only suggest fixes where needed, using no more than 10 lines of code total. "
            "Avoid full rewrites or non-critical suggestions."
        ), # Limit content preview
        agent=agents[1],
        expected_output=(
            "• List up to 4 critical security/performance risks (1-line each).\n"
            "• Avoid unnecessary code snippets.\n"
            "• Only provide fix if the issue is severe and fix is short (max 8–10 lines total)."
        )
    )
    
    task_3 = Task(
        description=f"Does {ext} file match the functionality document?\n\n{functionality_description}...\n\nCode:\n{file_content}...",  # Limit content preview
        agent=agents[2],
        instruction=(
        "You must NOT provide large code blocks. "
        "Only suggest fixes where needed, using no more than 10 lines of code total. "
        "Avoid full rewrites or non-critical suggestions."
        ),
        expected_output=(
        "• Describe in 4–5 lines if the file aligns with the functionality doc.\n"
        "• If something is missing, explain it briefly.\n"
        "• Avoid code unless absolutely necessary."
    )
    )
    
    return [task_1, task_2, task_3]