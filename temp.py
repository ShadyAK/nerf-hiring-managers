import requests

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + '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'
}
payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": """These are my skill sets : Java, Python, SQL, TypeScript, Sping Boot, Flask and I have 2 years of professional experience
The skills required for a job are : Python, Flask, Django, more than 1 year of experience
Write a message to hiring manager mentioning how I am a good fit for the role """}]
}

response = requests.post(url, headers=headers, json=payload)

print(response)