import os

class TextModerator:
    def __init__(self):
        self.model_path = "models/text_moderator/"
        # Checks if your partner has dropped a model config file yet
        self.is_ready = os.path.exists(os.path.join(self.model_path, "config.json"))

    def predict(self, text: str) -> dict:
        if not self.is_ready:
            return {"status": "mock_mode", "flagged": False, "confidence": 0.0, "message": "Waiting for trained model."}
        
        return {"status": "active", "flagged": True, "confidence": 0.95}