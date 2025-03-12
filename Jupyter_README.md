# Jupyter Notebook Setup for FastAPI_NER

This guide provides a detailed setup for running the **Named Entity Recognition (NER) model** in Jupyter Notebook. It covers installing dependencies, setting up the environment, training the model, and converting it to ONNX.
### Prerequisites
**Python3.10.0, jupyter, ipykernel**

Go to the Folder/Directory where you want to Clone the project
### 1️⃣ Clone the Repository
In the terminal:

```cmd
git clone https://github.com/Puran2006/FastAPI_NER.git
```
Move to the project folder FastAPI_NER
```cmd
cd FastAPI_NER
```

### 2️⃣ Create a Virtual Environment
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

## 3️⃣ Install Dependencies

Install all required dependencies using the `requirements.txt` file inside the main FastAPI_NER folder:
```sh
pip install -r requirements.txt
```

## 4️⃣ Install PyTorch (IMPORTANT!)

You **must install PyTorch separately** based on your system configuration. Visit the official [PyTorch website](https://pytorch.org/get-started/locally/) and choose the correct installation command.

For example, to install PyTorch with CUDA 11.8 support:
```sh
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
For CPU-only installation:
```sh
pip3 install torch torchvision torchaudio
```

## 5️⃣ Running Jupyter Notebook

Start Jupyter Notebook to train the model:
```sh
jupyter notebook
```

Then, open and run the **`model_preparation/model_training.ipynb`** notebook step by step.

The trained model and tokenizer are stored in the saved_pkl folder.

## 6️⃣ Convert Trained Model to ONNX

Once the training is complete, convert the model to ONNX format for optimized deployment:
```sh
python model_preparation/convert_to_onnx.py
```
The ner_model.onnx model is also stored in the saved_pkl fold
### **Why Convert to ONNX?**
- Reduces **Docker image size** when deploying with FastAPI.
- Optimized for inference across different platforms.
- Faster and more efficient model execution.

##  Additional Notes
- Ensure **CUDA is enabled** if using a GPU (`!nvidia-smi` in terminal to check).
- **Do NOT preprocess** text (no stopword removal, lemmatization, or lowercasing) before training.
- Always load the best-trained model (`best_bert_ner_model`) for inference.

---
Now you're ready to train and deploy your NER model! 🚀

