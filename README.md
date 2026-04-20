# 🎯 ProofHire — GitHub-Verified Job Matching

> Stop sending generic CVs. Start proving your skills.

ProofHire is a 4-agent LangGraph AI system that analyses your actual GitHub projects, matches them against job requirements, and generates evidence-based cover letters in German professional standard — all in under 60 seconds.

---

## 🚀 What Makes ProofHire Different

Most job tools just match keywords on a CV. ProofHire verifies your **actual code** on GitHub — proving your skills with real evidence, not just claims.

| Feature                  | Other Tools | ProofHire |

| GitHub code verification | ❌          | ✅ |
| Multi-agent AI pipeline  | ❌          | ✅ |
| Evidence-based matching  | ❌          | ✅ |
| CV + GitHub combined     | ❌          | ✅ |
| German-standard letters  | ❌          | ✅ |
| Application history      | ❌          | ✅ |

---

## 🤖 The 4-Agent Pipeline


GitHub Username + CV + Job Description
↓
Agent 1 — GitHub Analyser
Fetches real repos, verifies actual tech skills from code
↓
Agent 2 — CV Analyser
Extracts experience, education, achievements
↓
Agent 3 — Job Matcher
Calculates Technical Fit Score, identifies skill gaps
↓
Agent 4 — Cover Letter Writer
Generates tailored German-standard cover letter
↓
Output: Fit Score + Skill Analysis + Cover Letter (.docx / .txt)

---

## 🛠️ Tech Stack

- **LangGraph** — Multi-agent orchestration
- **Groq** — Ultra-fast LLM inference (llama-3.3-70b-versatile)
- **GitHub API** — Real code verification
- **Supabase** — Application history storage
- **Streamlit** — Web interface
- **python-docx** — Word document export

---

## ⚙️ Setup & Installation

### 1. Clone the repo

```bash
git clone https://github.com/HarshaBodhe/ProofHire.git
cd ProofHire
```

### 2. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install langgraph langchain langchain-groq requests python-dotenv streamlit supabase python-docx pypdf
```

### 4. Set up API keys

Copy `.env.example` to `.env` and fill in your keys:
GROQ_API_KEY=your_groq_api_key_here
GITHUB_TOKEN=your_github_token_here
SUPABASE_URL=your_supabase_url_here
SUPABASE_KEY=your_supabase_key_here

**Where to get your keys:**
- **Groq API key** — Free at [console.groq.com](https://console.groq.com)
- **GitHub Token** — GitHub → Settings → Developer Settings → Personal Access Tokens
- **Supabase** — Free at [supabase.com](https://supabase.com) → Settings → API

### 5. Set up Supabase table

Run this in Supabase SQL Editor:

```sql
CREATE TABLE job_applications (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    created_at TIMESTAMP DEFAULT NOW(),
    user_name TEXT,
    user_email TEXT,
    user_phone TEXT,
    user_location TEXT,
    user_linkedin TEXT,
    github_username TEXT,
    company_name TEXT,
    role_title TEXT,
    github_analysis TEXT,
    cv_summary TEXT,
    match_analysis TEXT,
    cover_letter TEXT
);

ALTER TABLE job_applications ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Allow all operations" ON job_applications
FOR ALL USING (true) WITH CHECK (true);
```

### 6. Run the app

```bash
.venv\Scripts\python.exe -m streamlit run app.py
```

Open browser at `http://localhost:8501`

---

## 📁 Project Structure

ProofHire/
│
├── app.py              # Streamlit web interface
├── job_agent.py        # 4-agent LangGraph pipeline
├── .env.example        # API key template
├── .gitignore          # Excludes .env and .venv
└── README.md           # This file

---

## 🎯 How To Use

1. Go to **Generate Application**
2. Enter your details and GitHub username
3. Upload your CV (PDF or Word) or paste it
4. Paste the job description
5. Click **Generate My Application**
6. Get your Fit Score, skill analysis and cover letter
7. Download as Word (.docx) or Text (.txt)
8. View all past applications in **My History**

---

## 🔒 Privacy & Security

- API keys stored in `.env` — never committed to GitHub
- GitHub data processed ephemerally — raw code not stored
- Application data stored securely in Supabase with RLS enabled

---

## 🌟 Author

**Harsha Bodhe**
MSc Data Science · University of Europe for Applied Sciences · Berlin

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Harsha_Bodhe-blue)](https://linkedin.com/in/harsha-bodhe)
[![GitHub](https://img.shields.io/badge/GitHub-HarshaBodhe-black)](https://github.com/HarshaBodhe)
[![SSRN](https://img.shields.io/badge/Research-SSRN_Publications-orange)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5950455)

---

*ProofHire v1.0 · April 2026 · Built with LangGraph + Groq + Supabase*

