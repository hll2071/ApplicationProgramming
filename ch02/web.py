from fastapi import FastAPI

from ch02.model import Champion
from data import get_champions

app = FastAPI()

@app.get("/")
def get_all() -> list[Champion]:
    return get_champions()



if __name__ == '__main__' :
    import uvicorn
    uvicorn.run("web:app",reload=True)