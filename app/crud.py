from sqlalchemy.orm import Session

import models
import schemas

def get_blogposts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.BlogPost).offset(skip).limit(limit).all()

def get_blogpost_by_id(db: Session, id: int):
    return db.query(models.BlogPost).filter(models.BlogPost.id == id).first()

def get_existing_blog_post(db: Session, author: str, title: str, content: str):
    return db.query(models.BlogPost).filter(
        models.BlogPost.author == author,
        models.BlogPost.title == title,
        models.BlogPost.content == content
    ).first()

def create_blog_post(db: Session, blogpost: schemas.BlogPost):
    db_post = models.BlogPost(**blogpost.model_dump())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_blog_post(db: Session, id: int, blogpost: schemas.BlogPostUpdate):
    db_post = db.query(models.BlogPost).filter(models.BlogPost.id == id).first()
    if db_post:
        for field, value in blogpost.model_dump(exclude_unset=True).items():
            setattr(db_post, field, value)
        db.commit()
        db.refresh(db_post)
    return db_post

def delete_blog_post(db: Session, post: models.BlogPost):
    db.delete(post)
    db.commit()

def clear_database(db: Session):
    # Gebruik de query.delete() methode om alle rijen uit de gewenste tabel te verwijderen
    db.query(models.BlogPost).delete()
    db.commit()