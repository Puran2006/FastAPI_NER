# FastAPI Named Entity Recognition (NER)

## 📌 Overview
Machine learning project focused on Named Entity Recognition (NER) using the CoNLL dataset. The project encompasses model training, a FastAPI-based backend for serving predictions, and a Streamlit-based frontend for user interaction.

FastAPI_NER is a lightweight and efficient Named Entity Recognition (NER) API built using **FastAPI**. It allows users to extract named entities (such as names, locations, organizations, and more) from text using a trained NLP model.

---

## 🛠 Manual Installation & Setup

### 1️⃣ Prerequisites
**Python 3.10, Docker, Git**

Go to the Folder/Directory where you want to Clone the project
### 2️⃣ Clone the Repository
In the terminal:

```cmd
git clone https://github.com/Puran2006/FastAPI_NER.git
```
Move to the project folder FastAPI_NER
```cmd
cd FastAPI_NER
```

### 3️⃣ Create a Virtual Environment
It is recommended to set up a virtual environment to manage dependencies.
While creating virtual environment makesure that you use Python 3.10 is used.  
Use the below command to find where python 3.10.0 is location

```cmd
where python
```
Expected Output (like this):
```cmd
C:\Users\puran\AppData\Local\Programs\Python\Python310\python.exe
```  
Use the path to create a environment
```cmd
C:\Users\puran\AppData\Local\Programs\Python\Python310\python.exe -m venv venv
source venv/bin/activate  # On macOS/Linux
.\venv\Scripts\activate  # On Windows
```
After setting up the environment you should see something like this:
```cmd
(env) C:\Users\puran\Desktop\Personal\FastAPI_NER>
```
Also check the python path and pip path of the environment to verify:
```cmd
where python
where pip
```
Ensure that the pip and python you are using are from the location inside of the virtual enviroment that we created

Once it is clear upgrade the pip
```cmd
pip install --upgrade pip
```

## 4️⃣ Dependencies  Dependency Management

The repository contains three separate `requirements.txt` files to handle dependencies efficiently:

1. **FastAPI Dependencies**  
   - 📂 Path: `FastAPI_NER/fastapi_app/requirements.txt`  
   - 📝 Contains dependencies required for running the **FastAPI backend**.
     
   **Install with:**  
   ```cmd
   pip install --no-cache-dir -r FastAPI_NER/fastapi_app/requirements.txt
   ```
   
2. **Streamlit Dependencies**  
   - 📂 Path: `FastAPI_NER/streamlit_app/requirements.txt`  
   - 📝 Contains dependencies required for running the **Streamlit frontend**.
     
   **Install with:**  
   ```cmd
   pip install --no-cache-dir -r FastAPI_NER/streamlit_app/requirements.txt
   ```

3. **All Project Dependencies**  
   - 📂 Path: `FastAPI_NER/requirements.txt`  
   - 📝 Contains all dependencies required for the entire project, including Jupyter Notebook dependencies for model training and conversion..
   - We will Install it later when we are setting up the ipynb file.
  
   **Install with:**  
   ```cmd
   pip install -r --no-cache-dir FastAPI_NER/requirements.txt
   ```
For now just install Fast api and Streamlit dependecies for running the API.


### 5️⃣ Run FastAPI Backend
Go to the fastapi_app folder
```cmd
cd fastapi_app
```
Run the command
```cmd
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
-- The API will be accessible at: [http://127.0.0.1:8000](http://127.0.0.1:8000)  or [http://localhost:8000](http://localhost:8000).  

-- Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  or [http://localhost:8000/docs](http://localhost:8000/docs) for the FastAPI swaggerUI.    

-- Input the text sentence in the /predict after authentication and exceute to see the response

#### 🔑 Authentication credentials: 
- **Username:** `admin`
- **Password:** `deccanai`


### 6️⃣ Run Streamlit Frontend
Open another terminal for opening Streamlit Folder and make sure to activate the virtual environment we have created.

```cmd
cd FastAPI_NER/streamlit_app/
```
```cmd
streamlit run app.py
```
This launches a web UI where users can log in and test NER.

#### 🔑 Streamlit Login Credentials
- **Username:** `admin`
- **Password:** `deccanai`
---

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

## 🚀 Deployment Options
You can deploy this FastAPI service on:
- **AWS EC2**
- **Google Cloud Run**
- **Heroku**
- **Azure Functions**

A proper Deployement strategy Using AWS EC2 is given in the Deployment_strategy.md in this repo itself

---

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Added new feature"`
4. Push to the branch: `git push origin feature-name`
5. Open a Pull Request

---

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file.

## 👨‍💻 Author
- **Puran2006** - [GitHub](https://github.com/Puran2006)

---
⭐ If you find this project useful, give it a star on GitHub! 🚀

