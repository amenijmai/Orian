import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).parent

class Config:
    ENV = os.getenv('ENV', 'development')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    EMAIL_PROVIDER = os.getenv('EMAIL_PROVIDER', 'mock')  # 'gmail', 'outlook', or 'mock'
    CRM_PROVIDER = os.getenv('CRM_PROVIDER', 'mock')
    CALENDAR_PROVIDER = os.getenv('CALENDAR_PROVIDER', 'mock')
    MEMORY_PATH = os.getenv('MEMORY_PATH', str(BASE_DIR / 'data' / 'memory.json'))
    DEFAULT_FOLLOWUP_DAYS = int(os.getenv('DEFAULT_FOLLOWUP_DAYS', '3'))
