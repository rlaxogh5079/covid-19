from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/clinics")
async def home():
    return {"message": "test"}

if __name__ == "__main__":
    uvicorn.run(app="server:app", host="localhost", port=8000, reload=True)
