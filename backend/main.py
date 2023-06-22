#uvicorn main:app
#uvicorn main:app --reload
#source venv/Scripts/activate


#Main Imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import openai

#custom Function Imports

#Initiate App
app = FastAPI()

# CORS - Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:3000",
]


# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Check Health
@app.get("/health")
async def check_health():
    return {"message": "healthy"}

#Post bot response 
# Note: Not playning in browser when using post request 
# @app.post ("/post-audio/")
# async def post_audio (file:UploadFile=File(...)):
#     print("hello")