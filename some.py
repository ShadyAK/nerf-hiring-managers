
import openai

openai.api_key = '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'

response = openai.Chat.create(
  model="gpt-3.5-turbo",
  prompt="""These are my skill sets : Java, Python, SQL, TypeScript, Sping Boot, Flask and I have 2 years of professional experience
The skills required for a job are : Python, Flask, Django, more than 1 year of experience
Write a message to hiring manager mentioning how I am a good fit for the role """,
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
)