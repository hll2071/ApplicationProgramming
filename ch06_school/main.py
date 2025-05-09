from fastapi import FastAPI,Request
from starlette.responses import JSONResponse

from ch06_school.error import SchoolException
from ch06_school.web import department as department_web
from ch06_school.web import student as student_web

app = FastAPI()
app.include_router(department_web.router)
app.include_router(student_web.router)
@app.exception_handler(SchoolException)
def school_exception_handler(request: Request, exc: SchoolException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success":False,
            "message": exc.msg
        }
    )

if __name__ == '__main__' :
    import uvicorn
    uvicorn.run("main:app", reload=True)