# app/schema.py

from pydantic import BaseModel

class EmailRequest(BaseModel):
    text: str


class PredictionResponse(BaseModel):
    label: str