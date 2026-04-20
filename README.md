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


## 🌟 Author

**Harsha Bodhe**
MSc Data Science · University of Europe for Applied Sciences · Berlin

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Harsha_Bodhe-blue)](https://linkedin.com/in/harsha-bodhe)
[![GitHub](https://img.shields.io/badge/GitHub-HarshaBodhe-black)](https://github.com/HarshaBodhe)
[![SSRN](https://img.shields.io/badge/Research-SSRN_Publications-orange)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5950455)

---

*ProofHire v1.0 · April 2026 · Built with LangGraph + Groq + Supabase*
