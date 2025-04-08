from fastapi import FastAPI, Body, Header

app = FastAPI()

@app.post("/hi")
def hello(who : str = Header()) :
    return f"Hello, {who}"

@app.get("/hi/{who}")
def greet(who):
    return f"Hello, {who}"

@app.get("/agent")
def get_agent(user_agent : str = Header()) :
    return user_agent

@app.get("/async")
async def ync() :
    import asyncio
    await asyncio.sleep(1)
    return "Hello, World"

if __name__ == "__main__" :
    import uvicorn
    uvicorn.run("hello:app", reload=True)