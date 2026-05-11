from fastapi import FastAPI,Request
from time import perf_counter
from routers import todo_router,user_router
import json

app=FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
        print(request['path'])
        print(request['method'])
        payload=await request.body()
        if payload:
              print(json.loads(payload))
        start_time = perf_counter()
        response = await call_next(request)
        process_time = perf_counter()
        print(start_time-process_time)
        return response

routers=[todo_router,user_router]
for router in routers:
    app.include_router(router=router,prefix="/api")