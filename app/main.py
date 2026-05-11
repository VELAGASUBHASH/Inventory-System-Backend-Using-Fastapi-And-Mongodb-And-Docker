
from fastapi import FastAPI
from app.routes.product_routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Inventory System API"
)
app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://inventorysystem-ruddy.vercel.app"
    ],

    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

@app.get("/")
async def home():
    return {
        "message":"Welcome ...."
    }


