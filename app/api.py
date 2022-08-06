from fastapi import FastAPI, Body, Depends

from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.auth_handler import signJWT
from app.auth.auth_bearer import JWTBearer

app = FastAPI(
    title="FastAPI - JWT Authentication",
    description="Example API in FastAPI. 🚀",
    version="1.0.0",
    contact={
        "name": "Cesar Steinmeier",
        "email": "cesssar@me.com"
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

users = []

posts = [
    {
        "id": 1,
        "title": "Título 1",
        "content": "Conteúdo 1"
    }
]

@app.get("/", tags=["root"])
async def root():
    return {"message": "Hello to my API"}

@app.get("/posts", tags=["posts"])
async def get_posts() -> dict:
     return { "data" : posts}

@app.get("/posts/{id}", tags=["posts"])
async def get_post(id: int) -> dict:
    if id > len(posts):
        return {"message": "Post not found"}
    for post in posts:
        if post["id"] == id:
            return { "data" : post}

@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return { "data" : "Post added"}

@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

@app.post("/user/login", tags=["user"])
async def login_user(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {"message": "Invalid credentials"}

