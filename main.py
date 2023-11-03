from fastapi import Depends, FastAPI, HTTPException
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
        raise HTTPException(status_code=404, detail="Blogpost not found")
    return blog_post

# POST-endpoint om een nieuwe blogpost aan te maken
@app.post('/posts/', response_model=schemas.BlogPost)
def create_new_blog_post(blogpost: schemas.BlogPostCreate, db: Session = Depends(get_db)):
    return crud.create_blog_post(db, blogpost)