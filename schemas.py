from pydantic import BaseModel

class BlogPostBase(BaseModel):
    id: int
    author: str | None = None
    title: str
    content: str

class BlogPostCreate(BlogPostBase):
    pass

class BlogPost(BlogPostBase):
    id: int

    class Config:
        orm_mode = True
