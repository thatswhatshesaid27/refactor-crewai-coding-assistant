
from crewai import Agent

def setup_crew():
    potential_tester = Agent(
        role="Potential Code Tester",
        goal="Only identify and explain critical syntax issues. Provide short fixes (if truly needed), not full code. Never exceed 5–10 lines in any fix.",
        backstory="An expert at identifying syntax issues in Python and web files.",
        model="gpt-4-turbo",
        temperature=0.0
    )
    
    senior_tester = Agent(
        role="Senior Security & Performance Tester",
        goal="Analyze the performance and security vulnerabilities, Provide short fixes (if truly needed), not full code. Never exceed 5–10 lines in any fix.",
        backstory="A security specialist and performance optimizer.",
        model="gpt-4-turbo",
        temperature=0.0
    )
    
    senior_fullstack_tester = Agent(
        role="Senior Full Stack Code Reviewer",
        goal="Validate business logic, API integrations, and architecture, dont provide huge coding solutions only address those issues and provide solutions for those which are necessary and which has small line of solutions needed,(maximum 5 to 6 lines)",
        backstory="An experienced software architect.",
        model="gpt-4-turbo",
        temperature=0.0
    )
    
    return [potential_tester, senior_tester, senior_fullstack_tester]
