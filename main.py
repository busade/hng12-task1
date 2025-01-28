from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials= True,
    allow_methods =["GET"],
    allow_headers=["*"]
)


@app.get('/dev')
def search():
    email = "adesolaisa3@gmail.com"
    current_datetime=datetime.now().isoformat()
    github_url ="github.com/busade/hng12-task1"
    response = {
        "email": email,
        "current_datetime" : current_datetime,
        "github_url": github_url,

    }
    return response
