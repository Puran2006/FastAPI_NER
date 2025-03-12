import torch
import onnx
import pickle
from transformers import BertTokenizerFast, BertForTokenClassification

# Load your model
with open('../saved_pkl/ner_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load your tokenizer
with open('../saved_pkl/tokenizer.pkl', 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

device = torch.device('cpu')
model.to(device)
model.eval()

text = "Barack Obama was the president of the United States."
encoding = tokenizer(text, 
                     truncation=True, 
                     padding='max_length', 
                     max_length=128, 
                     return_tensors='pt')

input_ids = encoding['input_ids'].to(device)
attention_mask = encoding['attention_mask'].to(device)

# Convert to ONNX
torch.onnx.export(
    model, 
    (input_ids, attention_mask),  # Inputs as a tuple
    "../saved_pkl/ner_model.onnx",  
    input_names=["input_ids", "attention_mask"],  
    output_names=["output"],  
    dynamic_axes={  
        "input_ids": {0: "batch_size"},  
        "attention_mask": {0: "batch_size"},  
        "output": {0: "batch_size"}  
    },  
    opset_version=14
)

print(" Model successfully converted to ONNX")
