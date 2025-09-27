# CHATBOT

A small FastAPI + Streamlit chatbot project.

## What this repo contains

- `app.py` - FastAPI application (HTTP API for the chatbot)
- `streamlit_app.py` - Streamlit UI for local testing
- `graph.py` - graph helper utilities used by the project

## Quick setup (Windows, PowerShell)

1. Create and activate a virtual environment (if you haven't):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies (example):

```powershell
.\venv\Scripts\python.exe -m pip install --upgrade pip
.\venv\Scripts\python.exe -m pip install fastapi uvicorn streamlit
```

3. Run the FastAPI server (from project root, not inside Python REPL):

```powershell
.\venv\Scripts\python.exe -m uvicorn app:app --reload --port 8000
```

4. Run the Streamlit UI (in a separate terminal):

```powershell
.\venv\Scripts\python.exe -m streamlit run streamlit_app.py
```

## Common issues

- If you see `SyntaxError` when running `uvicorn ...` make sure you ran it from PowerShell (not the Python interactive prompt). Exit the Python prompt with `exit()` or `Ctrl+Z` then Enter.
- If you get `Connection refused` when calling `http://127.0.0.1:8000`, ensure the server is running and listening on port 8000.

## Git / GitHub

1. Initialize and commit (already done in this workspace):

```powershell
git init
git add -A
git commit -m "Initial commit"
```

2. Add your GitHub remote and push (replace `<REMOTE_URL>`):

```powershell
git remote add origin <REMOTE_URL>
git branch -M main
git push -u origin main
```

If you prefer the GitHub CLI and it's authenticated locally you can run:

```powershell
gh repo create your-repo --public --source=. --remote=origin --push
```

## License

Add a license if you want to open-source this project.

---
If you want, I can also expand this README with examples, environment variables, or deployment instructions. Tell me which sections you'd like.
