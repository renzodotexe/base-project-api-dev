from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Simuleer enkele blogberichten
blog_posts = [
    {"id": 1, "title": "Mijn eerste blogpost", "content": "Dit is de inhoud van mijn eerste blogpost."},
    {"id": 2, "title": "Een andere blogpost", "content": "Dit is een tweede blogpost."},
    {"id": 3, "title": "Nog een blogpost", "author": "Renzo Lemmens", "content": "Dit is de derde blogpost."},
]

class BlogPost(BaseModel):
    id: int
    author: str | None = None
    title: str
    content: str

@app.get('/posts', response_model=List[BlogPost])
def get_posts():
    return blog_posts

