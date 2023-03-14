import requests

api_key = "3f169ce745964b1d86f94ea12ff4ad4c"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-02-14&sortBy=publishedAt&apiKey=" \
      "3f169ce745964b1d86f94ea12ff4ad4c"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
