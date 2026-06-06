from fastapi import FastAPI
from repository.user_repository import user_router
app=FastAPI()

app.include_router(user_router)

app.include_router(user_router)
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def get_users():
    return user_router.get_users()


