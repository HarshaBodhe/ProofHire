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

### 2. Create a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```bash
pip install langgraph langchain langchain-groq requests python-dotenv streamlit supabase python-docx pypdf
```

### 4. Set up API keys

Copy `.env.example` to `.env` and fill in your keys:

```bash
cp .env.example .env
```