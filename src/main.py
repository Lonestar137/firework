from fastapi import FastAPI

app = FastAPI()

NODES = {
    "Node1": {
        "Sub1": {},
        "Sub2": {},
        "Sub3": {},
    },
    "Node2": {
        "Sub1": {},
        "Sub2": {},
        "Sub3": {},
    },
}

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/")
async def root():
    return {"message": "Hello world"}
