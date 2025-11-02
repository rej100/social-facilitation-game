# Repository Guidelines

## Project Structure & Module Organization
The Streamlit app that powers the facilitation runs from `Facilitation-game.py`. It defines the round logic, scoring, and participant profiles; keep any new gameplay modules in the same directory for Streamlit to discover them. Source readings that inform the scenarios live in `articles/`. The facilitation and the game needs to be based on them. The `venv/` directory is a local virtual environment and should not be committed; 

## Build, Test, and Development Commands
- `python -m venv venv && source venv/bin/activate` creates and activates a local environment.
- `pip install streamlit pandas matplotlib` syncs dependencies used by the current app.
- `streamlit run Facilitation-game.py` launches the facilitation interface at `http://localhost:8501`.
- `streamlit run Facilitation-game.py --server.runOnSave true` enables live reload while iterating on content.