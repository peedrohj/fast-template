import sys

from fastapi import Request
from fastapi.responses import JSONResponse


async def exception_handler(
    request: Request, exception: Exception
) -> JSONResponse:
    return JSONResponse(
        content={'error': type(exception).__name__, 'message': str(exception)},
        status_code=500,
    )
