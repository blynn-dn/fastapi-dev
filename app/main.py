from fastapi import FastAPI
from app.routers import webhook
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

app = FastAPI()
app.include_router(webhook.router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get('/')
async def default():
    """redirect to /docs"""
    response = RedirectResponse(url='/docs')
    return response


if __name__ == '__main__':
    """if called as a command line app"""
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
