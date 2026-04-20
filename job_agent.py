import os
import requests
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from datetime import date

load_dotenv()

# ---- LLM SETUP ----
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# ---- STATE ----
class AgentState(TypedDict):
    github_username: str
    cv_text: str
    job_description: str
    github_analysis: str
    cv_summary: str
    match_analysis: str
    cover_letter: str
    user_name: str
    user_email: str
    user_phone: str
    user_location: str
    user_linkedin: str
    hiring_manager: str
    company_name: str
    company_address: str
    hiring_email: str
    role_title: str

# ---- AGENT 1: GITHUB ANALYSER ----
def github_analyser(state: AgentState) -> AgentState:
    print("\n🔍 Agent 1: Fetching GitHub Profile...")

    username = state['github_username']
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"⚠️ GitHub API error: {response.status_code} — skipping GitHub analysis")
        state['github_analysis'] = "GitHub profile could not be fetched. Analysis based on CV only."
        return state

    repos = response.json()

    if not isinstance(repos, list):
        print("⚠️ No repos found — skipping GitHub analysis")
        state['github_analysis'] = "No public repositories found. Analysis based on CV only."
        return state

    repo_info = []
    for repo in repos[:5]:
        repo_info.append({
            "name": repo.get("name"),
            "description": repo.get("description"),
            "language": repo.get("language"),
            "stars": repo.get("stargazers_count")
        })

    repo_text = "\n".join([
        f"- {r['name']} ({r['language']}): {r['description']} | Stars: {r['stars']}"
        for r in repo_info
    ])

    prompt = f"""
    You are a technical recruiter analysing a GitHub profile.

    GitHub Username: {username}

    Top Repositories:
    {repo_text}

    Based on these repositories provide:
    1. Primary programming languages used
    2. Key technical skills demonstrated
    3. Types of projects built
    4. Overall technical level assessment
    5. Notable achievements

    Be specific and evidence-based.
    """

    response = llm.invoke(prompt)
    state['github_analysis'] = response.content
    print("✅ GitHub Analysis complete!")
    return state

# ---- AGENT 2: CV ANALYSER ----
def cv_analyser(state: AgentState) -> AgentState:
    print("\n📄 Agent 2: Analysing CV...")

    prompt = f"""
    You are a professional CV analyst.

    Analyse this CV and extract:
    1. Key technical skills
    2. Work experience and roles
    3. Education background
    4. Notable projects and achievements
    5. Soft skills and competencies

    CV:
    {state['cv_text']}

    Provide a clear structured summary.
    """

    response = llm.invoke(prompt)
    state['cv_summary'] = response.content
    print("✅ CV Analysis complete!")
    return state

# ---- AGENT 3: JOB MATCHER ----
def job_matcher(state: AgentState) -> AgentState:
    print("\n🎯 Agent 3: Matching Profile to Job...")

    prompt = f"""
    You are an expert technical job matcher.

    GITHUB ANALYSIS:
    {state['github_analysis']}

    CV SUMMARY:
    {state['cv_summary']}

    JOB DESCRIPTION:
    {state['job_description']}

    Provide a detailed matching report:
    1. Technical Fit Score (0-100%)
    2. Top 3 matching skills with evidence
    3. Skill gaps or missing requirements
    4. Strengths that stand out
    5. Overall recommendation (Strong/Good/Partial fit)

    Base your score on BOTH GitHub evidence AND CV experience.
    Be specific about which projects/experience supports each point.
    """

    response = llm.invoke(prompt)
    state['match_analysis'] = response.content
    print("✅ Job Matching complete!")
    return state

# ---- AGENT 4: COVER LETTER WRITER ----
def cover_letter_writer(state: AgentState) -> AgentState:
    print("\n✍️ Agent 4: Writing Cover Letter...")

    today = date.today().strftime("%d %B %Y")

    if state['hiring_manager']:
        recipient_block = f"{state['hiring_manager']}\n{state['company_name']}\n{state['company_address']}"
        salutation = f"Dear {state['hiring_manager']},"
    else:
        recipient_block = f"{state['company_name']}\n{state['company_address']}"
        salutation = "Dear Hiring Team,"

    hiring_email_line = f"\n{state['hiring_email']}" if state['hiring_email'] else ""

    prompt = f"""
    You are an expert cover letter writer specialising in German professional standards.

    Write a formal German-standard cover letter using EXACTLY this format:

    ---
    {state['user_name']}
    {state['user_location']}
    {state['user_email']}
    {state['user_phone']}
    {state['user_linkedin']}

    {today}

    To:
    {recipient_block}{hiring_email_line}

    Re: Application — {state['role_title']}

    {salutation}

    [Write 3-4 compelling paragraphs here]

    Kind regards,
    {state['user_name']}
    ---

    Use this information to write the body:

    GITHUB EVIDENCE:
    {state['github_analysis']}

    CANDIDATE PROFILE:
    {state['cv_summary']}

    JOB MATCH ANALYSIS:
    {state['match_analysis']}

    JOB DESCRIPTION:
    {state['job_description']}

    The cover letter body must:
    - Open with a strong hook referencing the specific role at {state['company_name']}
    - Reference specific GitHub projects as technical evidence
    - Address the job requirements directly
    - Show genuine motivation for {state['company_name']} specifically
    - Be professional, concise and compelling
    - End with a clear call to action
    - Follow strict German business letter format
    """

    response = llm.invoke(prompt)
    state['cover_letter'] = response.content
    print("✅ Cover Letter complete!")
    return state

# ---- BUILD LANGGRAPH ----
def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("github_analyser", github_analyser)
    graph.add_node("cv_analyser", cv_analyser)
    graph.add_node("job_matcher", job_matcher)
    graph.add_node("cover_letter_writer", cover_letter_writer)

    graph.set_entry_point("github_analyser")
    graph.add_edge("github_analyser", "cv_analyser")
    graph.add_edge("cv_analyser", "job_matcher")
    graph.add_edge("job_matcher", "cover_letter_writer")
    graph.add_edge("cover_letter_writer", END)

    return graph.compile()

# ---- MAIN ----
if __name__ == "__main__":
    print("🚀 ProofHire — GitHub-Verified Job Matching")
    print("="*50)
    print("Welcome! Please provide your details below.\n")

    print("--- YOUR DETAILS ---")
    user_name = input("Full Name (e.g. Max Müller): ")
    user_email = input("Email (e.g. max.muller@gmail.com): ")
    user_phone = input("Phone Number (e.g. +49 155 12345678): ")
    user_location = input("City, Country (e.g. Berlin, Germany): ")
    user_linkedin = input("LinkedIn URL (e.g. linkedin.com/in/maxmuller): ")
    github_username = input("GitHub Username — no spaces (e.g. MaxMuller): ")

    print("\n--- PASTE YOUR CV ---")
    print("Paste your CV text below. When done type 'END' on a new line:")
    cv_lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        cv_lines.append(line)
    cv_text = "\n".join(cv_lines)

    print("\n--- PASTE JOB DESCRIPTION ---")
    print("Paste the job description below. When done type 'END' on a new line:")
    jd_lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        jd_lines.append(line)
    job_description = "\n".join(jd_lines)

    print("\n--- JOB DETAILS ---")
    role_title = input("Role Title (e.g. AI Engineering Intern): ")
    company_name = input("Company Name (e.g. Mercedes-Benz): ")
    company_address = input("Company Address (or press Enter to skip): ")

    print("\n--- HIRING MANAGER (optional — press Enter to skip) ---")
    hiring_manager = input("Hiring Manager Name (or press Enter to skip): ")
    hiring_email = input("Hiring Manager Email (or press Enter to skip): ")

    initial_state = AgentState(
        github_username=github_username,
        cv_text=cv_text,
        job_description=job_description,
        github_analysis="",
        cv_summary="",
        match_analysis="",
        cover_letter="",
        user_name=user_name,
        user_email=user_email,
        user_phone=user_phone,
        user_location=user_location,
        user_linkedin=user_linkedin,
        hiring_manager=hiring_manager,
        company_name=company_name,
        company_address=company_address,
        hiring_email=hiring_email,
        role_title=role_title
    )

    app = build_graph()
    print("\n🤖 Starting ProofHire 4-Agent Pipeline...\n")
    result = app.invoke(initial_state)

    print("\n" + "="*50)
    print("🔍 GITHUB ANALYSIS:")
    print("="*50)
    print(result['github_analysis'])

    print("\n" + "="*50)
    print("📄 CV SUMMARY:")
    print("="*50)
    print(result['cv_summary'])

    print("\n" + "="*50)
    print("🎯 JOB MATCH ANALYSIS & FIT SCORE:")
    print("="*50)
    print(result['match_analysis'])

    print("\n" + "="*50)
    print("✉️ GENERATED COVER LETTER:")
    print("="*50)
    print(result['cover_letter'])

    with open("results.txt", "w", encoding="utf-8") as f:
        f.write("GITHUB ANALYSIS:\n" + result['github_analysis'])
        f.write("\n\nCV SUMMARY:\n" + result['cv_summary'])
        f.write("\n\nJOB MATCH ANALYSIS:\n" + result['match_analysis'])
        f.write("\n\nCOVER LETTER:\n" + result['cover_letter'])

    print("\n✅ Results saved to results.txt!")