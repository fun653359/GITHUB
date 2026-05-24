from fastapi import FastAPI, Form, UploadFile, File
from fastapi.responses import RedirectResponse, FileResponse
import os
from pathlib import Path

app = FastAPI()

UPLOAD_DIR = Path.cwd() / "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
async def redirect_to_index():
    return RedirectResponse(url="/index.html")

@app.get("/index.html")
async def index_html():
    return FileResponse("index.html")

@app.post("/submit")
async def submit(
    name: str = Form(...),
    number: str = Form(...),
    phone_number: str = Form(...),
    donge: str = Form(...),
    file: UploadFile = File(...)   # ← str 에서 UploadFile 로 수정
):
    # 파일 저장
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)

    return {
        "name": name,
        "number": number,
        "phone_number": phone_number,
        "donge": donge,
        "saved_file": str(file_path)   # 저장 경로 반환
    }