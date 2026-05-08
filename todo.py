from fastapi import FastAPI
from routers import todo_router,user_router

app=FastAPI()
routers=[todo_router,user_router]
for router in routers:
    app.include_router(router=router,prefix="/api")