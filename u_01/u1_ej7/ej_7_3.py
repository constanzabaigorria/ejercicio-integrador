from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserCreate(UserBase):
    password: str


class UserPublic(UserBase):
    pass


@app.post("/users/", response_model=UserPublic, status_code=201)
async def create_user(user: UserCreate) -> UserPublic:
    return UserPublic(**user.model_dump())