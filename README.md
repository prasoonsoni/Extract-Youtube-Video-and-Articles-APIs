# Extract-Youtube-Video-and-Articles-APIs
Creators:
1. Prasoon Soni
2. Rishi Kaushal

An API for fetching YouTube videos and articles with the particular keywords given by user.
```
BASE_URL = https://happify-me-api.herokuapp.com
```

### Endpoints
1. For Fetching Youtube Videos
```
URL = BASE_URL/getvideos
```
Result
```json
{
    "video_results": [
        {
            "channel_link": "CHANNEL_LINK",
            "channel_logo": "CHANNEL_LOGO",
            "channel_name": "CHANNEL_NAME",
            "video_description": "VIDEO_DESCRIPTION",
            "video_length": "VIDEO_LENGTH",
            "video_link": "VIDEO_LINK",
            "video_thumbnail": "VIDEO_THUMBNAIL",
            "video_title": "VIDEO_TITLE"
        },]
}
```
---
2. For Fetching Articles
```
URL = BASE_URL/getarticles
```
Result
```json
{
    "article_results": [
        {
            "article_description": "ARTICLE_DESCRIPTION",
            "article_link": "ARTICLE_LINK",
            "article_title": "ARTICLE_TITLE",
            "link_to_display": "LINK_TO_DISPLAY"
        },]
}
```
---
### Data to be sent in body.
```json
{
  "api_key":"YOUR_SERPAPI_KEY",
  "keyword":"YOUR_KEYWORD_TO_SEARCH"
}
```
