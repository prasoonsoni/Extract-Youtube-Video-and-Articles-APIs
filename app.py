from serpapi import GoogleSearch
from requests import request
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return(
        "<h1>Welcome to API.</h1>"+
        "<p>/getvideos - to get video links.</p>"+
        "<p>/getarticles - to get article links.</p>"
    )

@app.route("/getvideos", methods=['POST'])
def get_video_results():
    data = request.json
    keyword = data["keyword"]
    api_key = data["api_key"]
    params = {
      "api_key": api_key,
      "engine": "youtube",
      "search_query": keyword
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    video_results = results["video_results"]
    final_result = []
    for video in video_results:
        video_length = video["length"]
        video_length = video_length.split(":")
        if(int(video_length[0])<=5):
            video_data = {
                "channel_link":video["channel"]["link"],
                "channel_name":video["channel"]["name"],
                "channel_logo":video["channel"]["thumbnail"],
                "video_description":video["description"],
                "video_length":video["length"],
                "video_link":video["link"],
                "video_thumbnail":video["thumbnail"]["static"],
                "video_title":video["title"]
            }
            final_result.append(video_data)
        else:
            pass
    return({"video_results":final_result})


@app.route("/getarticles", methods=['POST'])
def get_articles_results():
    data = request.json
    keyword = "articles about " + data["keyword"]
    api_key = data["api_key"]
    params = {
        "q": keyword,
        "hl": "en",
        "gl": "us",
        "api_key": api_key
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    organic_articles = results["organic_results"]
    articles = []
    for article in organic_articles:
        data = {
            "article_title":article["title"],
            "link_to_display":article["displayed_link"],
            "article_link":article["link"],
            "article_description":article["snippet"]
        }
        articles.append(data)

    return {"article_results":articles}
    