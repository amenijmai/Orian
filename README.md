# Orion - Agentic Business Assistant

Orion is an **Agentic Business Assistant** scaffold implemented in Python. It provides a modular framework to orchestrate tasks, interact with email, calendar, CRM systems, and maintain a simple memory store. This is a reference implementation meant to be adapted and connected to real APIs. Sensitive credentials are loaded from environment variables.

## Files

- `main.py` - Entrypoint
- `config.py` - Configuration and environment helpers
- `outils.py` - Utility helpers (email parsing, text utils)
- `memory.py` - Simple file-based memory store
- `agent.py` - Core agent orchestration and decision loop
- `clients/email_client.py` - Email adapter (Gmail/Outlook) – simple wrapper/stub
- `clients/calendar_client.py` - Calendar adapter
- `clients/crm_client.py` - CRM adapter (HubSpot/Salesforce stub)
- `prompts.py` - Prompt templates
- `requirements.txt` - Python dependencies
- `run_local.sh` - Quick-run script

## Installation

1. Create a Python virtual environment:

```bash
python -m venv .venv
```

2. Activate the virtual environment:

- macOS/Linux:

```bash
source .venv/bin/activate
```

- Windows:

```bash
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

- Set environment variables in a `.env` file (see `config.py` comments for details).
- Sensitive credentials (email, CRM, API keys) should **never** be committed to GitHub.

## Usage

Run the assistant in preview mode:

```bash
python main.py --mode=preview
```

## Notes

- This project is a scaffold / reference implementation.
- Adapters (`email_client.py`, `calendar_client.py`, `crm_client.py`) are stubs and should be connected to real APIs for production use.
- Memory is file-based (`memory.py`) for simplicity; you may replace it with a database or other storage.

## License

Specify your license here (e.g., MIT, Apache 2.0).

## Contributing

Feel free to fork the project, adapt the adapters, and submit pull requests to improve functionality.
