from fastapi import APIRouter, status

health_router = APIRouter(prefix='', tags=['Health'])


@health_router.get(path='/health', status_code=status.HTTP_200_OK)
def health():
    """
    The health check route for this api
    """
    return True
