from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import logging

security = HTTPBasic()
logger = logging.getLogger(__name__)

# Basic Auth Credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "deccanai"

# Authenticate Function
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    logger.info(f"Authentication Attempt: {credentials.username}")
    
    if credentials.username != VALID_USERNAME or credentials.password != VALID_PASSWORD:
        logger.warning("Authentication Failed")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials. Please provide valid username/password.",
            headers={"WWW-Authenticate": "Basic"},
        )
    logger.info("Authentication Successful")
    return credentials.username
