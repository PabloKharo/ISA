import sys
sys.path.append('../../backend')

from fastapi import FastAPI, HTTPException

from common.database import db
from common.tables.account import *
from common.tables.message import *
from common.tables.dialogue import *

app = FastAPI()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# API для создания диалога
@app.post("/dialogues/")
def create_dialogue(user1_login: str, user2_login: str):
    user1 = db.query(Account).filter(Account.login == user1_login).first()
    user2 = db.query(Account).filter(Account.login == user2_login).first()
    if not user1 or not user2:
        raise HTTPException(status_code=404, detail="One or both users not found")

    new_dialogue = Dialogue(account1_id=user1.id, account2_id=user2.id)
    db.add(new_dialogue)
    db.commit()
    db.refresh(new_dialogue)
    return {"dialogue_id": new_dialogue.id}

# API для получения списка диалогов
@app.get("/dialogues/{login}")
def get_dialogues(login: str):
    user = db.query(Account).filter(Account.login == login).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    dialogues = db.query(Dialogue).filter((Dialogue.account1_id == user.id) | (Dialogue.account2_id == user.id)).all()
    return [{"dialogue_id": dialogue.id, "other_user_login": dialogue.account1.login if dialogue.account1_id != user.id else dialogue.account2.login} for dialogue in dialogues]

# API для получения списка сообщений диалога
@app.get("/messages/{dialogue_id}")
def get_messages(dialogue_id: int):
    dialogue = db.query(Dialogue).filter(Dialogue.id == dialogue_id).first()
    if not dialogue:
        raise HTTPException(status_code=404, detail="Dialogue not found")

    messages = [{"body": message.body, "author": message.author.login, "date": message.date} for message in dialogue.messages]
    return messages

# API для создания сообщения
@app.post("/messages/")
def create_message(dialogue_id: int, body: str, author_login: str):
    dialogue = db.query(Dialogue).filter(Dialogue.id == dialogue_id).first()
    if not dialogue:
        raise HTTPException(status_code=404, detail="Dialogue not found")

    author = db.query(Account).filter(Account.login == author_login).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    new_message = Message(dialogue_id=dialogue.id, body=body, author_id=author.id)
    db.add(new_message)
    db.commit()
    return {"message": "Message sent successfully"}
