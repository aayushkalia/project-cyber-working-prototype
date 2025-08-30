from pydantic import BaseModel

class AnalyzeResponse(BaseModel):
    apk_id: str
    label: str
    explanation: str
