import os
import time

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse
from dotenv import load_dotenv

import uvicorn


app = FastAPI()
load_dotenv()


class Model(BaseModel):
    text: str

@app.post("/convert")
async def convert_text_to_html(text: Model):
    file_name = f"{int(time.time())}_result.html"
    with open(f"static/{file_name}", "w") as f:
        f.write(text.text)
    download_url = f"http://{os.getenv('SERVER_HOST')}:8000/download/{file_name}"
    return download_url

@app.get("/download/{file_name}")
async def download_html(file_name: str):
    return FileResponse(f"static/{file_name}", filename=file_name, media_type="text/html")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)