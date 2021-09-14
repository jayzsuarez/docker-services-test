from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()


@app.get("/")
async def root():
    r = requests.get("http://client-api:6089/")
    return r.json()


@app.get("/test")
async def test():
    return {"message": "/test from cards-api"}


if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=6088, reload=True)



