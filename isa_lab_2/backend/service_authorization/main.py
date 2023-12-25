import sys
sys.path.append('../../backend')

from fastapi import FastAPI, HTTPException

from common.database import db
from common.tables.account import *

app = FastAPI()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# API для создания нового пользователя
@app.post("/users/")
def create_user(account: AccountCreate):
    db_account = db.query(Account).filter(Account.login == account.login).first()
    if db_account is None:
        raise HTTPException(status_code=404, detail="User with login already exists")
    db_account = Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return {"message": "User created successfully"}

# API для поиска пользователя по логину
@app.get("/users/{login}")
def get_user_by_login(login: str):
    db_account = db.query(Account).filter(Account.login == login).first()
    if db_account is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_account

# API для поиска пользователя по маске имени и фамилии
@app.get("/users/")
def get_user_by_name_mask(last_name: str, first_name: str):
    db_accounts = db.query(Account).filter(Account.last_name.like(f"%{last_name}%"), Account.first_name.like(f"%{first_name}%")).all()
    if not db_accounts:
        raise HTTPException(status_code=404, detail="Users not found")
    return db_accounts


