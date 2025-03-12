from pydantic import BaseModel
from typing import List, Dict

class PredictionRequest(BaseModel):
    text: str

    class Config:
        json_schema_extra = {
            "example": {
                "text": "Elon Musk is the CEO of Tesla"
            }
        }

class PredictionResponse(BaseModel):
    text: str
    entities: List[Dict[str, str]]

    class Config:
        json_schema_extra = {
            "example": {
                "text": "Elon Musk is the CEO of Tesla",
                "entities": [
                    {"token": "Elon", "entity": "B-PER"},
                    {"token": "Musk", "entity": "I-PER"},
                    {"token": "Tesla", "entity": "B-ORG"}
                ]
            }
        }
