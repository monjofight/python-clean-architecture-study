from fastapi.security import OAuth2PasswordBearer

# 認証スキームの設定
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")