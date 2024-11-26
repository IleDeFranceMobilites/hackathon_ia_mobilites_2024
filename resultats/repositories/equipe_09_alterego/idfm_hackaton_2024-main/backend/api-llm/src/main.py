from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .nlu import Nlu

app = FastAPI()

# Need to specify the list of ports, else it won't work with only "*"
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://10.244.1.53:5173",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

nlu = Nlu()

class MessageRequest(BaseModel):
    message: str

@app.post("/get_intentions_entites")
async def get_intentions_entites(request: MessageRequest):
    answer = nlu.get_intentions_entites(request.message)
    return JSONResponse(content={"answer": answer})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)