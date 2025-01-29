from fastapi import FastAPI
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware
import pytz

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials= True,
    allow_methods =["GET"],
    allow_headers=["*"]
)

timezone = pytz.timezone("Africa/Lagos")
@app.get('/')
def search():
    email = "adesolaisa3@gmail.com"
    current_datetime=(datetime.now()).isoformat()+ "Z"
    github_url ="https://github.com/busade/hng12-task1"
    response = {
        "email": email,
        "current_datetime" : current_datetime,
        "github_url": github_url,

    }
    return response
