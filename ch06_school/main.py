from fastapi import FastAPI
from ch06_school.web import department as department_web

app = FastAPI()
app.include_router(department_web.router)

if __name__ == '__main__' :
    import uvicorn
    uvicorn.run("main:app", reload=True)