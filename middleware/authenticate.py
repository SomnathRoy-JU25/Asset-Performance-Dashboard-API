from fastapi import HTTPException, Request
from config.settings import API_KEY

# middleware/authenticate.py
async def authenticate(request: Request):
    auth_token = request.headers.get("Authorization")
    if not auth_token or auth_token != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
