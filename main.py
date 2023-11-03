from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dit is een geheime sleutel of token voor ontwikkelaars
DEVELOPER_API_KEY = "Munano123!"

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET-endpoint om alle blogposts op te halen
@app.get('/posts/', response_model=list[schemas.BlogPost])
def get_all_blog_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    blog_posts = crud.get_blogposts(db, skip=skip, limit=limit)
    return blog_posts

# GET-endpoint om een specifieke blogpost op te halen op basis van ID
@app.get('/posts/{post_id}', response_model=schemas.BlogPost)
def get_blog_post_by_id(post_id: int, db: Session = Depends(get_db)):
    blog_post = crud.get_blogpost_by_id(db, post_id)
    if blog_post is None:
        raise HTTPException(status_code=404, detail="Requested blogpost ID not found.")
    return blog_post

# POST-endpoint om een nieuwe blogpost aan te maken
@app.post('/posts/', response_model=schemas.BlogPost)
def create_new_blog_post(blogpost: schemas.BlogPostCreate, db: Session = Depends(get_db)):
    # Controleer of een identieke post al bestaat
    existing_post = crud.get_existing_blog_post(db, blogpost.author, blogpost.title, blogpost.content)
    if existing_post:
        raise HTTPException(status_code=400, detail="A blogpost with the same values already exists.")
    return crud.create_blog_post(db, blogpost)

# PUT-endpoint om een bestaande blogpost aan te passen
@app.put('/posts/{post_id}', response_model=schemas.BlogPost)
def update_blog_post_by_id(post_id: int, blogpost: schemas.BlogPostUpdate, db: Session = Depends(get_db)):
    updated_post = crud.update_blog_post(db, post_id, blogpost)
    if updated_post is None:
        raise HTTPException(status_code=404, detail="Requested blogpost ID not found.")
    return updated_post

# Endpoint om de hele database te wissen (alleen voor ontwikkelaars)
@app.post("/clear-database/")
async def clear_whole_database(api_key: str = Query(..., title="API Key")):
    if api_key != DEVELOPER_API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized Access!")

    # Wis de database
    db = SessionLocal()
    crud.clear_database(db)
    return {"message": "Database wiped! This cannot be undone."}
