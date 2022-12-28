from fastapi import FastAPI


app = FastAPI()

posts = []

@app.get('/')
def read_root():
    return {"hello":"Hello World"}


@app.get('/posts')
def get_posts():
    return posts