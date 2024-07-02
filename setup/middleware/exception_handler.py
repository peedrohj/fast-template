import sys

from fastapi import Request
from fastapi.responses import JSONResponse


async def exception_handler(request: Request, exc: Exception) -> JSONResponse:
    exception_type, exception_value, _ = sys.exc_info()
    exception_name = getattr(exception_type, '__name__', None)

    return JSONResponse(
        content={'error': exception_name, 'message': str(exception_value)},
        status_code=500,
    )
