If you want to pull and run the image directly from **Docker Hub**, use the following commands:
# Prerequisites
**Docker**
## Docker PULL
```cmd
docker pull puran2006/fastapi-app:latest
```

Run the container:
```cmd
docker run -p 8000:8000 puran2006/fastapi-app:latest
```

The API will now be accessible at:
- [http://127.0.0.1:8000](http://127.0.0.1:8000)
- [http://localhost:8000](http://localhost:8000)

Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the API.

##  Run Streamlit Frontend
Open another terminal for opening Streamlit Folder and make sure to activate the virtual environment we have created.
```cmd
cd FastAPI_NER/streamlit_app/
```
Install the requirements.txt:
```cmd
pip install --no-cache-dir -r requirements.txt
```
```cmd
streamlit run app.py
```
This launches at accessible at: [http://127.0.0.1:8501](http://127.0.0.1:8501)  or [http://localhost:8501](http://localhost:8501) web UI where users can log in and test NER.

#### 🔑 Streamlit Login Credentials
- **Username:** `admin`
- **Password:** `deccanai`
---
