# PyTorch container with Python 3.10 and CUDA 12.6
FROM python:3.10-slim

# Working directory in the container 
WORKDIR /fastapi_app

# Copy the requirements.txt file into the 
COPY requirements.txt .

# Upgrade pip to the latest version
RUN pip install --upgrade pip

RUN pip install onnxruntime

# Installing all the dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy the entire Fastapi directory contents into the container
COPY . .

# Expose port 8000 to allow external access
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


