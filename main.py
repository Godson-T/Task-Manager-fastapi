from fastapi import FastAPI,Depends,HTTPException
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
@app.get("/task")
def get_tasks(db:Session=Depends(get_db)):
    tasks=db.query(models.Task).all()
    return tasks

@app.get("/task/{task_id}")
def get_single_task(task_id: int,db:Session=Depends(get_db)):
    task=db.query(models.Task).filter(
        models.Task.id== task_id
    ).first()
    
    if not task:
        raise HTTPException(status_code=404, details="Task not found")
    return task
