from fastapi import FastAPI,Request
from time import perf_counter
from routers import todo_router,user_router
import json
from slowapi import  Limiter
from slowapi.util import get_remote_address #user ko ip address lina
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app=FastAPI()

# creating the limiter object
limiter=Limiter(key_func=get_remote_address) #   takes the ip addess and keeps the time record of people when they visit the api endpoint

app.state.limiter=limiter # now we can access this limiter object 
app.add_exception_handler(
      RateLimitExceeded,
      lambda request, exc :JSONResponse(
            status_code=429,
            content={"message":"too many request"}
            
      ) 

)

app.add_middleware(SlowAPIMiddleware)

app.state.api_counter=0

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
        print(request['path'])
        print(request['method'])
        payload=await request.body()
        if payload:
              print(json.loads(payload))
        start_time = perf_counter()
        app.state.api_counter+=1
        response = await call_next(request)
        process_time = perf_counter()
        print(start_time-process_time)
        return response

routers=[todo_router,user_router]
for router in routers:
    app.include_router(router=router,prefix="/api")