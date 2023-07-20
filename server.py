from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.security.api_key import APIKeyHeader, APIKey
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import chatbot

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
API_KEY = os.getenv("API_KEY")
if API_KEY is None:
    raise EnvironmentError("API_KEY not found in .env file")

app = FastAPI()

# Define API key name and its location (header)
API_KEY_NAME = "X-API-KEY-Token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# Model for the request payload
class MessageRequest(BaseModel):
    user_message: str

# Secure endpoint that requires API key authentication
@app.post("/secure_endpoint/")
async def secure_endpoint(message_request: MessageRequest, api_key: APIKey = Depends(api_key_header)):
    user_message = message_request.user_message
    print(user_message)
    if api_key == API_KEY:
        result = chatbot.conv(user_message)
        return {"answer": result}
    else:
        raise HTTPException(status_code=403, detail="Could not validate credentials")
