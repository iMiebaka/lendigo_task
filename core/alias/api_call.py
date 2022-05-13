import requests
from core import db, models

def first_batch(length=100):
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
    result = response.json()
    if models.Post.query.all() is None:
        return result
    return result[-length:]

def get_news(id):
    response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json')
    result = response.json()
    return result
    print(response.json()["kids"])

def get_comments(id, post_id):
    response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json')
    result = response.json()
    try:
        comment = models.Comments(
            by = comment["by"],
            public_id = comment["id"],
            parent_id = post_id,
            text = comment["text"],
            time = comment["time"],
        )
        db.session.add(comment)
        db.session.commit()
    except: 
        pass

