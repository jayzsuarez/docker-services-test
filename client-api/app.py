from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()


@app.get("/")
async def root():

    return {"message": "/test from client-api"}


@app.get("/test")
async def test():
    r = requests.get("http://card-api:6088/test")
    return r.json()


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=6089, reload=True)



