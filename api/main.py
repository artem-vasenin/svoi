from fastapi import FastAPI, Query
import uvicorn
from typing import Optional
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class SPerson(BaseModel):
    lst: str
    firstName: str
    lastName: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Vue dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mansLst = [
    {"id": 1, "firstName": "Petr", "lastName": "Petrov"},
    {"id": 2, "name": "Serg", "lastName": "Sergeevich"},
]
womenLst = [
    {"id": 1, "name": "Ira", "lastName": "Petrova"},
    {"id": 2, "name": "Lena", "lastName": "Sergeeva"},
]

@app.get("/{lst}", response_model=list[SPerson])
async def get_list(
        lst: str,
        limit: Optional[int] = Query(5, ge=1, le=20),
    ):
    if lst == "man":
        return mansLst[:limit] if limit else mansLst
    elif lst == "women":
        return womenLst[:limit] if limit else womenLst
    else:
        return []
@app.get("/")
async def show_home() -> str:
    return 'Hello from API!'
@app.post("/")
async def add_to_list(data: SPerson) -> SPerson:
    if data.lst == "man":
        mansLst.append({"id": 3, "firstName": data.firstName, "lastName": data.lastName})
        return data
    elif data.lst == "women":
        womenLst.append({"id": 3, "firstName": data.firstName, "lastName": data.lastName})
        return data
    else:
        return None

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
