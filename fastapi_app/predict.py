from fastapi import APIRouter, Depends, HTTPException
from transformers import BertTokenizerFast
import logging
from schemas import PredictionRequest, PredictionResponse
from model_tokenizer import load_model_and_tokenizer
from auth import authenticate
import numpy as np

tag_list = ['O', 'B-PER', 'I-PER', 'B-ORG', 'I-ORG', 'B-LOC', 'I-LOC', 'B-MISC', 'I-MISC'] 
model, tokenizer = load_model_and_tokenizer()


def get_tokenizer():
    return tokenizer

router = APIRouter()
# Predict Function - Handles NER Prediction
@router.post("/predict", response_model=PredictionResponse, dependencies=[Depends(authenticate)])
def predict(
    input: PredictionRequest,
    tokenizer: BertTokenizerFast = Depends(get_tokenizer)
):
    try:
        logging.info(f"Prediction request received")
        logging.info(f"Input text: {input.text}")

        # Tokenize the input text
        inputs = tokenizer(input.text, 
                           return_tensors="np", 
                           truncation=True, 
                           padding='max_length', 
                           max_length=128)

        # Convert to NumPy (ONNX only accepts NumPy arrays)
        input_ids = inputs['input_ids'].astype(np.int64)
        attention_mask = inputs['attention_mask'].astype(np.int64)

        outputs = model.run(None, {
            "input_ids": input_ids,
            "attention_mask": attention_mask
        })

        # Extract logits
        logits = outputs[0]
        predictions = np.argmax(logits, axis=-1).squeeze().tolist()

        #  Extract tokens (with subwords like ##on)
        tokens = tokenizer.convert_ids_to_tokens(input_ids[0])

        #  Merge subwords and capture entities
        current_entity = ""
        current_label = ""
        entities = []

        for i, token in enumerate(tokens):
            if i == 0 or token in ["[PAD]", "[CLS]", "[SEP]"]:
                continue

            label_index = predictions[i]
            entity_name = tag_list[label_index]

            # Ignore "O" tokens
            if entity_name == "O":
                # If we were previously capturing an entity, save it now
                if current_entity:
                    entities.append({
                        "token": current_entity.strip(),
                        "entity": current_label
                    })
                    current_entity = ""
                    current_label = ""
                continue

            # If it's a subword like "##on", merge it
            if token.startswith("##"):
                current_entity += token.replace("##", "")
            else:
                # If it's a new entity, push the old one (if any)
                if current_entity:
                    entities.append({
                        "token": current_entity.strip(),
                        "entity": current_label
                    })
                    current_entity = ""
                    current_label = ""

                # Start a new entity
                current_entity += token
                current_label = entity_name

        # Catch any remaining entity
        if current_entity:
            entities.append({
                "token": current_entity.strip(),
                "entity": current_label
            })
        logging.info(f"Prediction successful")
        logging.info(f"Extracted Entities: {entities}")
        #  Return response
        return PredictionResponse(
            text=input.text,
            entities=entities
        )

    except Exception as e:
        logging.error(f"Prediction failed")
        logging.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")