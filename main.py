from fastapi import FastAPI, Query, HTTPException
from pathlib import Path

app = FastAPI()

FILE_PATH = "/dados/meuarquivo.txt"

def read_file():
    path = Path(FILE_PATH)
    if not path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()

@app.get("/content")
def get_content():
    return {"lines": read_file()}

@app.get("/lines")
def get_line_count():
    return {"count": len(read_file())}

@app.get("/search")
def search(keyword: str = Query(..., min_length=1)):
    lines = read_file()
    matches = [line.strip() for line in lines if keyword.lower() in line.lower()]
    return {"matches": matches}
