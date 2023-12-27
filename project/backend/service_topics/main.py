import sys
sys.path.append('../../backend')

from fastapi import FastAPI, HTTPException

from common.database import db
from common.tables.account import *
from common.tables.topic import *

app = FastAPI()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# API для создания поста
@app.post("/topics/")
def create_topic(author_login: str, body: str):
    author = db.query(Account).filter(Account.login == author_login).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    new_topic = Topic(author_id=author.id, body=body)
    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)
    return {"topic_id": new_topic.id}

# API для получения списка постов пользователя
@app.get("/topics/user/{user_login}")
def get_user_topics(user_login: str):
    user = db.query(Account).filter(Account.login == user_login).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    topics = db.query(Topic).filter(Topic.author_id == user.id).all()
    return [{"topic_id": topic.id, "author": topic.author.login, "body": topic.body, "date": topic.date} for topic in topics]

# API для получения поста
@app.get("/topics/{topic_id}")
def get_topic(topic_id: int):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")

    return {"author": topic.author.login, "body": topic.body, "date": topic.date}

# API для изменения поста
@app.put("/topics/{topic_id}")
def update_topic(topic_id: int, author_login: str, body: str):
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")

    author = db.query(Account).filter(Account.login == author_login).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    if topic.author_id != author.id:
        raise HTTPException(status_code=403, detail="You are not authorized to update this topic")

    topic.body = body
    topic.change_date = datetime.utcnow()
    db.commit()
    return {"message": "Topic updated successfully"}
