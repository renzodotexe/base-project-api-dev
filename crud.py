from sqlalchemy.orm import Session

import models
import schemas

def get_blogposts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.BlogPost).offset(skip).limit(limit).all()

def get_blogpost_by_id(db: Session, id: int):
    return db.query(models.BlogPost).filter(models.BlogPost.id == id).first()

def create_blog_post(db: Session, author: str, title: str, content: str):
    db_post = models.BlogPost(author=author, title=title, content=content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
