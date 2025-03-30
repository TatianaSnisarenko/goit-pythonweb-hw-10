from fastapi import APIRouter, Depends, Request
from schemas import User
from services.auth import get_current_user
from slowapi import Limiter
from slowapi.util import get_remote_address

router = APIRouter(prefix="/users", tags=["users"])
limiter = Limiter(key_func=get_remote_address)


@router.get("/me", response_model=User)
@limiter.limit("5/minute")
async def me(request: Request, user: User = Depends(get_current_user)):
    """
    Get details of the currently authenticated user.
    - Requires a valid access token in the `Authorization` header.
    - Requests are limited up to 5 per minute.
    """
    return user
