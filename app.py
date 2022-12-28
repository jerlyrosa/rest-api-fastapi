from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid


app = FastAPI()

posts = []


# Post Model

class Post(BaseModel):
    id: Optional[str]
    title: str
    autor: str
    content: Text
    created_text: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool


@app.get('/')
def read_root():
    return {"hello": "Hello World"}


@app.get('/posts')
def get_posts():
    return posts


@app.post('/posts')
def save_post(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return posts[-1]


@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post['id'] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post Not Found")


@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            posts.pop(index)
            return {"message": "Post has been deleted success"}
    raise HTTPException(status_code=404, detail="Post Not Found")


@app.put('/posts/{post_id}')
def update_post(post_id: str, updatedPost: Post):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            posts[index]['title'] = updatedPost.title
            posts[index]['content'] = updatedPost.content
            posts[index]['autor'] = updatedPost.autor
            return {"message": "Post has been updated success"}
    raise HTTPException(status_code=404, detail="Post Not Found")
