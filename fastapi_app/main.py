from fastapi import FastAPI, Request, HTTPException, Depends
from predict import router as predict_router
import logging
import os
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from auth import authenticate

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_DIR = os.path.join(BASE_DIR, "logs")

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

# Logging Configuration
logging.basicConfig(
    filename=os.path.join(LOGS_DIR, 'app.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

security = HTTPBasic()
logger = logging.getLogger(__name__)

# Create FastAPI Application
app = FastAPI()

# Include the Predict Router with Authentication
app.include_router(predict_router, tags=["predict"])

# Application Startup Logging
@app.on_event("startup")
def startup_event():
    logger.info("FastAPI application has started successfully.")

# Application Shutdown Logging
@app.on_event("shutdown")
def shutdown_event():
    logger.info("FastAPI application has shut down.")

#Middleware to log every incoming request
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response Status: {response.status_code}")
    return response

# Root Endpoint (No Authentication Required)
@app.get("/")
def read_root():
    return {"message": "Welcome to the NER Prediction API!"}

# Get logs endpoint
@app.get("/get_logs", tags=["Logs"])
def get_logs(credentials: HTTPBasicCredentials = Depends(authenticate)):
    log_file_path = os.path.join(LOGS_DIR, 'app.log')
    
    # Check if log file exists
    if not os.path.exists(log_file_path):
        raise HTTPException(status_code=404, detail="Log file not found")
    
    try:
        with open(log_file_path, 'r') as log_file:
            logs = log_file.read()
        logger.info("Logs retrieved successfully.")
        return {"logs": logs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading log file: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    logging.info("Fast api is running on http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
