from pydantic import BaseModel

class BlogPostBase(BaseModel):
    author: str | None = None
    title: str
    content: str

class BlogPostUpdate(BlogPostBase):
    title: str | None = None
    content: str | None = None

class BlogPostCreate(BlogPostBase):
    pass

class BlogPost(BlogPostBase):
    id: int

    class Config:
        orm_mode = True
