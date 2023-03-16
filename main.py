import requests
from email_send import send_email

topic = "tesla"

api_key = "3f169ce745964b1d86f94ea12ff4ad4c"
url = f"https://newsapi.org/v2/everything?q={topic}" \
      f"&from=2023-02-15&sortBy=publishedAt&" \
      f"apiKey=3f169ce745964b1d86f94ea12ff4ad4c&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = "Subject: Today's news" + "\n"
# Access the article titles and description
for article in content["articles"][:20]:
    if article['title'] is not None:
        body = body + article["title"] + "\n"\
               + article["description"] + "\n"\
               + article["url"] + 2*"\n"

body = body.encode("utf8")
send_email(message=body)