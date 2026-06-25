from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from apps.pipeline.moderator import TextModerator

app = FastAPI(title="ModShield AI Gateway")
moderator = TextModerator()

class ContentPayload(BaseModel):
    content: str
    user_id: str

# 🏠 New Plain UI Homepage Route
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>ModShield AI</title>
            <style>
                body {
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f9fafb;
                    color: #111827;
                }
                .container {
                    text-align: center;
                }
                h1 {
                    font-size: 2.5rem;
                    margin-bottom: 0.5rem;
                }
                p {
                    color: #6b7280;
                    font-size: 1.1rem;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>ModShield AI</h1>
                <p>Updating soon...</p>
            </div>
        </body>
    </html>
    """

@app.post("/api/v1/moderate")
def moderate_text(payload: ContentPayload):
    result = moderator.predict(payload.content)
    return {
        "user_id": payload.user_id,
        "analysis": result
    }