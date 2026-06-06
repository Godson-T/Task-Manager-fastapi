from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import engine,get_db
import models,schemas

models.Base.metadata.create_all(bind=engine)
app=FastAPI()

@app.get("/")
def root():
    return {"message":"Sampletest"}
@app.get("/health")
def health():
    return {"status":"Working"}
@app.post("/task")
def create_task(task:schemas.TaskCreate,db:Session=Depends(get_db)):
    db_task=models.Task(
        title=task.title,
        description=task.description,
        completed=task.completed
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task