from typing import List, Dict, Any
import re
from dateutil import parser as dateparser

def simple_summarize(text: str, max_chars: int = 300) -> str:
    # naive summarizer: take first N chars and end at sentence boundary
    snippet = text.strip()[: max_chars]
    last_period = snippet.rfind('.')
    if last_period != -1 and last_period > max_chars * 0.6:
        snippet = snippet[: last_period + 1]
    return snippet

def detect_intent(subject: str, body: str) -> str:
    """Very simple intent detector based on keywords."""
    s = (subject + ' ' + body).lower()
    if any(w in s for w in ['meeting', 'schedule', 'calendar', 'call']):
        return 'schedule'
    if any(w in s for w in ['invoice', 'bill', 'payment']):
        return 'billing'
    if any(w in s for w in ['proposal', 'quote', 'rfp']):
        return 'opportunity'
    if any(w in s for w in ['thanks', 'thank you']):
        return 'thanks'
    return 'general'

def extract_dates(text: str):
    # crude: attempt to parse any date-like substrings
    candidates = re.findall(r"\b(?:on\s)?(\w+\s\d{1,2}(?:,\s\d{4})?)", text)
    dates = []
    for c in candidates:
        try:
            dt = dateparser.parse(c, fuzzy=True)
            dates.append(dt)
        except Exception:
            continue
    return dates
