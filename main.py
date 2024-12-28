# 샘플 Python 스크립트입니다.

# Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.


# def print_hi(name):
    # 스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.
#     print(f'Hi, {name}')  # 중단점을 전환하려면 Ctrl+F8을(를) 누릅니다.


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조


from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from domain.question import question_router
from domain.answer import answer_router
from domain.user import user_router

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://bak2.allparts.co.kr:8000",
    "http://59.15.58.85:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/hello")
# def hello():
#     return {"message": "안녕하세요 파이보"}

app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)

app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))


@app.get("/")
def index():
    return FileResponse("frontend/dist/index.html")