from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from classes import Item

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "hello from api"}

@app.post("/post-items/")
async def post_item(item: Item):
    with open("storage/items.txt", "a") as f:
        f.write(f"{repr(item)}\n")
    print(f"{repr(item)} \t wrote")
    return {"message" : "done"}

@app.get("/get-items")
async def get_items():
    try:
        with open("storage/items.txt", "r") as f:
            items = {}
            lines = f.readlines()
            for i in range(len(lines)):
                items[i] = lines[i]
            return items
    except FileNotFoundError:
        return {"error" : "file is not exist"}

