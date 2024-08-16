import fastapi
from . import user


router = fastapi.APIRouter()
router.include_router(user.router, prefix="/users")