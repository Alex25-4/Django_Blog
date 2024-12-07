import requests
from django.shortcuts import render


# Helper function to fetch news
def fetch_news():
    api_key = "23f63bdc2109408bb999c57ba65c420d"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        news_data = response.json()
        return news_data.get("articles", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")  # Debugging log
        return []


# Views for the application
def home(request):
    articles = fetch_news()[:6]  # Limit to 6 articles for the homepage
    return render(request, "blog/home.html", {"articles": articles})


def more_news(request):
    articles = fetch_news()  # All articles
    return render(request, "blog/more_news.html", {"articles": articles})


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return render(request, "blog/contact.html")
