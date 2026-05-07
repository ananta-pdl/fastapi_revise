

from fastapi import FastAPI

app=FastAPI()

@app.get("/",
         summary="this is a defult endpoint, that checks the condition of the api",
         description="i am started writing a backed for my todo application"
)

async def default():
    return {"Hi Samira, how you are feeling after dicthing me::"}

