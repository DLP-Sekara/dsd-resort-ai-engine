# pyrefly: ignore [missing-import]
from fastapi import APIRouter, HTTPException
# pyrefly: ignore [missing-import]
from pydantic import BaseModel, Field
from engines.demand_forecaster import DemandForecaster

router = APIRouter(prefix="/api/v1/forecast", tags=["Demand Forecasting"])

forecaster = DemandForecaster()

class ForecastRequest(BaseModel):
    DayOfWeek: int = Field(..., ge=0, le=6, description="0=Monday, 6=Sunday")
    IsWeekend: int = Field(..., ge=0, le=1, description="0 or 1")
    IsHoliday: int = Field(..., ge=0, le=1, description="0 or 1")
    Temperature: float = Field(..., description="Temperature in Celsius")
    Weather: str = Field(..., description="Clear, Cloudy, or Rainy")

@router.post("/")
def predict_guest_demand(request: ForecastRequest):
    try:
        input_data = request.model_dump()
        
        predicted_guests = forecaster.predict(input_data)
        
        return {
            "status": "success",
            "predicted_guest_count": predicted_guests,
            "message": "Demand forecast generated successfully."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))