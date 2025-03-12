# Jupyter Notebook Setup for FastAPI_NER

This guide provides a detailed setup for running the **Named Entity Recognition (NER) model** in Jupyter Notebook. It covers installing dependencies, setting up the environment, training the model, and converting it to ONNX.

## 1️⃣ Setup Environment

First, clone the repository:
```sh
git clone https://github.com/Puran2006/FastAPI_NER.git
cd FastAPI_NER
```

Create a virtual environment (recommended):
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

## 2️⃣ Install Dependencies

Install all required dependencies using the `requirements.txt` file inside the main FastAPI_NER folder:
```sh
pip install -r requirements.txt
```

## 3️⃣ Install PyTorch (IMPORTANT!)

You **must install PyTorch separately** based on your system configuration. Visit the official [PyTorch website](https://pytorch.org/get-started/locally/) and choose the correct installation command.

For example, to install PyTorch with CUDA 11.8 support:
```sh
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
For CPU-only installation:
```sh
pip3 install torch torchvision torchaudio
```

## 4️⃣ Running Jupyter Notebook

Start Jupyter Notebook to train the model:
```sh
jupyter notebook
```

Then, open and run the **`model_preparation/model_training.ipynb`** notebook step by step.

## 5️⃣ Convert Trained Model to ONNX

Once the training is complete, convert the model to ONNX format for optimized deployment:
```sh
python model_preparation/convert_to_onnx.py
```

### **Why Convert to ONNX?**
- Reduces **Docker image size** when deploying with FastAPI.
- Optimized for inference across different platforms.
- Faster and more efficient model execution.

## 6️⃣ Additional Notes
- Ensure **CUDA is enabled** if using a GPU (`!nvidia-smi` in terminal to check).
- **Do NOT preprocess** text (no stopword removal, lemmatization, or lowercasing) before training.
- Always load the best-trained model (`best_bert_ner_model`) for inference.

---
Now you're ready to train and deploy your NER model! 🚀

