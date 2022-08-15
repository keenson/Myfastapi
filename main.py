from typing import List
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException
from models import User, Gender, Role, UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("e674f7f9-9cb5-44b5-9f3b-88670217bdb5"),
        first_name="Jamila",
        last_name="Ahmed",
        gender= Gender.female,
        roles=[Role.student]
         ),
    User(
        id=UUID("ad5d81b8-75a2-422b-8236-d97aec66edb8"),
        first_name="Alex",
        last_name="Jones",
        gender= Gender.male,
        roles=[Role.admin,Role.user]
         )
]


@app.get("/")
def root():
    return {"Hello": "keenson"}


@app.get("/api/v1/users")
def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
        )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update:UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
        )
            