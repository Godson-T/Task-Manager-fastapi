from fastapi import FastAPI,Depends,HTTPException,Request 
from sqlalchemy.orm import Session
from database import engine,get_db
import models,schemas
from auth import hash_password,verify_token
from auth import verify_password, create_access_token
from fastapi.templating import Jinja2Templates


models.Base.metadata.create_all(bind=engine)
app=FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def root(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/task")
def create_task(task: schemas.TaskCreate, 
                db: Session = Depends(get_db),
                current_user: str = Depends(verify_token)):
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
def get_tasks(db:Session=Depends(get_db),current_user: str = Depends(verify_token)):
    tasks=db.query(models.Task).all()
    return tasks

@app.get("/task/{task_id}")
def get_single_task(task_id: int,db:Session=Depends(get_db),current_user: str = Depends(verify_token)):
    task=db.query(models.Task).filter(
        models.Task.id== task_id
    ).first()
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/task/{task_id}")
def edit_task(
    task_id: int,
    updated_task: schemas.TaskCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(verify_token)
):
    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = updated_task.title
    task.description = updated_task.description
    task.completed = updated_task.completed

    db.commit()
    db.refresh(task)

    return task
@app.delete("/task/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(verify_token)
):
    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Task deleted"}
@app.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    hashed = hash_password(password)
    db_user = models.User(username=username, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created", "username": db_user.username}


@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(username)
    return {"access_token": token, "token_type": "bearer"}