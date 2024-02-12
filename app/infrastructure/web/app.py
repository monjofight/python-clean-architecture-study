from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.infrastructure.web.routers import user_router

load_dotenv()


app = FastAPI()

# CORSの設定
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 許可するオリジン
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # 許可するHTTPメソッド
    allow_headers=[
        "X-Requested-With",
        "Content-Type",
        "Authorization",
    ],  # 許可するヘッダー
)


# ルーターの追加
app.include_router(user_router.router)
