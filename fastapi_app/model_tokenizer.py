import os
import pickle
from fastapi import HTTPException
import logging
import onnxruntime

#  Use the global app.log file
logger = logging.getLogger(__name__)


BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(BASE_DIR, "pkl_files", "ner_model.onnx")
TOKENIZER_PATH = os.path.join(BASE_DIR, "pkl_files", "tokenizer.pkl")


# Function to load the model and tokenizer
def load_model_and_tokenizer():
    try:
        logger.info(" Loading model and tokenizer...")

        session = onnxruntime.InferenceSession(MODEL_PATH)

        with open(TOKENIZER_PATH, 'rb') as tokenizer_file:
            tokenizer = pickle.load(tokenizer_file)
        logger.info("Model and tokenizer loaded successfully")
        return session, tokenizer

    except FileNotFoundError:
        logger.error(" Model or tokenizer file not found")
        raise HTTPException(status_code=500, detail="Model or Tokenizer file not found.")
    except Exception as e:
        logger.error(f"Unexpected error while loading model/tokenizer: {str(e)}")
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")


