# pyrefly: ignore [missing-import]
from fastapi import APIRouter, HTTPException
# pyrefly: ignore [missing-import]
from pydantic import BaseModel
from engines.nlp_engine import NLPAnalyzer

router = APIRouter(prefix="/api/v1/nlp", tags=["Sentiment Analysis"])

analyzer = NLPAnalyzer()
class ReviewRequest(BaseModel):
    review_text: str

@router.post("/analyze")
def analyze_review(data: ReviewRequest):
    try:
        label, confidence = analyzer.analyze(data.review_text)
        return {
            "status": "success",
            "review": data.review_text,
            "sentiment_label": label,
            "confidence_score": confidence
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))