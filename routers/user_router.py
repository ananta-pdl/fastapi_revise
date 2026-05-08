
from fastapi import APIRouter

user_router=APIRouter(
    prefix="/user",
    tags=["user"]
)

@user_router.get("/signin")

def signin():
    return {"you have signin successfully"}

@user_router.get("/signup")

def signup():
    return ("you have successfully signup")


