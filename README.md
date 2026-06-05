# Wine Pairing Agent

A small LangGraph agent that reads a recipe, recommends wines, and explains the pairing logic.

The LLM call uses MiniMax through its OpenAI-compatible Chat Completions API:

- Base URL: `https://api.minimax.io/v1`
- Default model: `MiniMax-M3`
- API key: loaded from `.env` or environment variables

## Run with your existing virtual environment

From this folder:

```powershell
& 'C:\Users\gos\project\nursing-record-assistant\.venv\Scripts\python.exe' -m wine_pairing_agent.cli --recipe "Grilled salmon with lemon butter, asparagus, and dill"
```

Or pass a recipe file:

```powershell
& 'C:\Users\gos\project\nursing-record-assistant\.venv\Scripts\python.exe' -m wine_pairing_agent.cli --file .\examples\salmon.txt
```

## Environment

`.env` is ignored by Git. Use `.env.example` as the template when deploying or cloning elsewhere.

```powershell
$env:MINIMAX_API_KEY="..."
$env:MINIMAX_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL="MiniMax-M3"
```

## GitHub setup later

This project is already ready for Git. When you tell me your GitHub repo URL, the binding commands will be:

```powershell
git init
git add .
git commit -m "Initial wine pairing agent"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

Before pushing, run `git status --ignored` and confirm `.env` is ignored.
