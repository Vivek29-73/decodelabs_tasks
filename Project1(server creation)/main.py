from fastapi import FastAPI
app=FastAPI()

@app.get("/",status_code=200)
def home():
    return {"message":"server is running"}

users=[
    {
    "id":1,
    "name":"vivek"
}
]

@app.get("/users",status_code=200)
def get_users():
    return {
        "users":users
    }

@app.post("/users",status_code=201)
def create_user():
    new_user={
        "id":len(users)+1,
        "name":"Adarsh"
    }

    users.append(new_user)

    return {
        "message":"user created successfully",
        "user":new_user
    }