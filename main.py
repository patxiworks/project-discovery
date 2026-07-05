from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Project(BaseModel):
    title: str
    description: str
    industry: str

@app.post("/projects")
def create_project(project: Project):
    return {
        "received": project
    }
