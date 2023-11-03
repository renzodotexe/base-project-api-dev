from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class BlogPost(Base):
    __tablename__ = "blogposts"

    id = Column(Integer, primary_key=True, index=True)
    author = Column(String)
    title = Column(String)
    content = Column(String)