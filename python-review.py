import requests
import json
import markdown2
import os

url = "https://review-o-matic.p.rapidapi.com/review"

with open("./python-test.py", "r") as file:
    code = file.read()

json_code = json.dumps(code)

payload = { "code": json_code }
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "YOUR-API-KEY",
	"X-RapidAPI-Host": "review-o-matic.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

json_review = json.loads(response.text)

review = json_review.get("review", "")

html_review = markdown2.markdown(review)

markdown_review = markdown2.markdown(html_review, extras=["markdown-in-html"])

with open("./review.md", "w") as file:
    file.write(markdown_review)

with open("./review.html", "w") as file:
    file.write(html_review)
    
