from fastapi import FastAPI

app = FastAPI(title="tellMe API", version="0.1.0")


@app.get("/v1/ping")
def ping():
    return {"mensaje": "tellMe backend funcionando"}