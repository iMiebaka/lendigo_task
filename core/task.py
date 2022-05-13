from threading import Thread
from time import sleep
from core import celery, models, db, shared_task, app
from core.alias.api_call import first_batch, get_news, get_comments
from datetime import datetime
import ast


# Runn every 5 mins
@shared_task
def get_post():
    for _ in first_batch():
        if models.PostId.query.filter_by(public_id=_).first() is None:
            post_id = models.PostId(public_id=_)
            db.session.add(post_id)
            db.session.commit()
            news = get_news(_)
            print(news)
            
            if news["type"] == "story":
                if "text" in news and "url" in news:
                    post = models.Post(
                    by = news["by"],
                    descendants = news["descendants"],
                    public_id = news["id"],
                    score = news["score"],
                    time = news["time"],
                    title = news["title"],
                    text = news["text"],
                    url = news["url"],
                    )
                    db.session.add(post)
                elif "url" in news:
                    post = models.Post(
                        by = news["by"],
                        descendants = news["descendants"],
                        public_id = news["id"],
                        score = news["score"],
                        time = news["time"],
                        title = news["title"],
                        url = news["url"],
                    )
                    db.session.add(post)
                elif "text" in news:
                    post = models.Post(
                    by = news["by"],
                    descendants = news["descendants"],
                    public_id = news["id"],
                    score = news["score"],
                    time = news["time"],
                    title = news["title"],
                    text = news["text"],
                    )
                    db.session.add(post)
                else:
                    pass
                db.session.commit()
                if "kids" in news:
                    for kids_q in news["kids"]:
                        thread = Thread(target= get_comments, args=[kids_q, post.id])
                        thread.start()
                    
                    find_type = models.Type.query.filter_by(name=news["type"]).first()
                    if find_type is None:
                        type_ = models.Type(
                            name = news["type"],
                        )
                        db.session.add(type_)
                        post.type = type_.id
                    else:
                        post.type = find_type.id
                    db.session.commit()
                print('Story Entered')
            else:
                print('Comment Passed')

