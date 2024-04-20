# external imports
import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# internal imports
sys.path.append(str(Path(__file__).parent.parent))
from src.lib.types import RequestBody

# create FastAPI app
app = FastAPI()


# definne the root route
@app.get("/")
async def root_get() -> dict[str, str]:
    return {"message": "Hello World"}


@app.post("/events")
async def root_post(body: RequestBody) -> dict[str, str]:
    return JSONResponse(content={"message": body.content})


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
    )
