from typing import Optional, List

from fastapi import FastAPI, status, Query
from pydantic import BaseModel
import uvicorn


app = FastAPI(title='Test environments')


class BasicMessage(BaseModel):
    message: str


@app.get(
    path='/',
    response_model=List[BasicMessage],
    status_code=status.HTTP_200_OK
)
async def home(
    name: Optional[str] = Query(None, min_length=1, max_length=79),
    times: int = Query(1, ge=1, le=15),
    message: Optional[str] = Query(None, min_length=4, max_length=255)
):
    if name is None:
        name = "World"

    if message is None:
        message = "Hello"

    message += (" " + name)
    messages = []

    for _ in range(times):
        messages.append(BasicMessage(message=message))

    return messages


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8005, reload=True)
