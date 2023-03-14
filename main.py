import requests
from send_email import send_email

api_key = "3f169ce745964b1d86f94ea12ff4ad4c"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-02-14&sortBy=publishedAt&apiKey=" \
      "3f169ce745964b1d86f94ea12ff4ad4c"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

body = ""
# Access the article titles and description
for article in content["articles"]:
    if article['title'] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf8")
send_email(message=body)