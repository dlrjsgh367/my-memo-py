import pathlib
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from database import Base, engine
from routes import user

# FastAPI 앱 생성
app = FastAPI()

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

# 정적 파일 경로 설정
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# 로그인 페이지 제공
@app.get("/login", response_class=HTMLResponse)
async def login():
    login_path = pathlib.Path("app/static/login.html")
    return login_path.read_text()


# 회원가입 페이지 제공
@app.get("/register", response_class=HTMLResponse)
async def register():
    register_path = pathlib.Path("app/static/register.html")
    return register_path.read_text()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
