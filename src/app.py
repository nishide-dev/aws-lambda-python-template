# external imports

import uvicorn
from fastapi import FastAPI

# internal imports
from src.lib.types import RequestBody

# create FastAPI app
app = FastAPI()


# definne the root route
@app.get("/")
async def root_get() -> dict[str, str]:
    return {"message": "Hello World"}


@app.post("/")
async def root_post(body: RequestBody) -> dict[str, str]:
    return {"message": body.content}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )
