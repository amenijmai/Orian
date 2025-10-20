"""
Prompt templates for LLM interactions. Keep concise and deterministic where possible.
"""
EMAIL_SUMMARY_PROMPT = (
"You are Orion, an executive assistant. Summarize the email for quick action:"
)


EMAIL_REPLY_PROMPT = (
"You are Orion, an assistant. Write a professional reply based on the email below."
)


MEETING_PREP_PROMPT = (
"You are Orion. Produce a 3-bullet meeting brief with context from past interactions."
)