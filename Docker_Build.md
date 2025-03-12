## 📤 Running with Docker
Go to the folder of fastapi_app

```cmd
cd FastAPI_NER/fastapi_app/
```
Make sure docker is running, If not then : 
```cmd
docker desktop start
```
To build the docker image, run this command:
```cmd
docker build -t fastapi-ner .
```
Verify the Image with:
```cmd
docker images
```
After verification run the docker image:
```cmd
docker run -p 8000:8000 fastapi-ner
```
-- The API will be accessible at: [http://127.0.0.1:8000](http://127.0.0.1:8000)  or [http://localhost:8000](http://localhost:8000).  

-- Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  or [http://localhost:8000/docs](http://localhost:8000/docs) for the FastAPI swaggerUI. 


###  Run Streamlit Frontend
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
