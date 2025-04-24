from fastapi import FastAPI
from api import user_api
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# app.include_router(news.router)
# app.include_router(products.router)
app.include_router(user_api.router)
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
