# pyrefly: ignore [missing-import]
from fastapi import FastAPI
# pyrefly: ignore [missing-import]
from fastapi.middleware.cors import CORSMiddleware
from routers import forecast_router
from routers.nlp_router import router as nlp_router
# pyrefly: ignore [missing-import]
import uvicorn

app = FastAPI(
    title="DSD AI Engine API",
    description="Machine Learning Backend for Restaurant Guest Demand Forecasting",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(forecast_router.router)
app.include_router(nlp_router)

@app.get("/")
def root():
    return {"message": "DSD AI Engine is running successfully!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)