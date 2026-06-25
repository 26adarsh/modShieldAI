from fastapi import FastAPI
from pydantic import BaseModel
from apps.pipeline.moderator import TextModerator

app = FastAPI(title="ModShield AI Gateway")
moderator = TextModerator()

class ContentPayload(BaseModel):
    content: str
    user_id: str

@app.post("/api/v1/moderate")
def moderate_text(payload: ContentPayload):
    result = moderator.predict(payload.content)
    return {
        "user_id": payload.user_id,
        "analysis": result
    }