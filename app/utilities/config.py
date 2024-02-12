from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_default_secret")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    ALGORITHM: str = "HS256"


settings = Settings()
