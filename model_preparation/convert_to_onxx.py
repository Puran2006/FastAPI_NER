import torch
import onnx
import pickle
from transformers import BertTokenizerFast, BertForTokenClassification

# Load the trained NER model (saved in .pkl format)
with open('../saved_pkl/ner_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the tokenizer
with open('../saved_pkl/tokenizer.pkl', 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

# Move model to CPU for inference and exporting
device = torch.device('cpu')
model.to(device)
model.eval()  # Set model to evaluation mode

# Example input sentence for testing
text = "Barack Obama was the president of the United States."

# Tokenize the input text (same preprocessing used during training)
encoding = tokenizer(
    text, 
    truncation=True, 
    padding='max_length', 
    max_length=128, 
    return_tensors='pt'
)

# Extract input tensors
input_ids = encoding['input_ids'].to(device)
attention_mask = encoding['attention_mask'].to(device)

# Convert the model to ONNX format
torch.onnx.export(
    model, 
    (input_ids, attention_mask),  # Model inputs as a tuple
    "../saved_pkl/ner_model.onnx",  # Save the ONNX model
    input_names=["input_ids", "attention_mask"],  # Define input names
    output_names=["output"],  # Define output name
    dynamic_axes={  
        "input_ids": {0: "batch_size"},  # Allow variable batch size
        "attention_mask": {0: "batch_size"},  
        "output": {0: "batch_size"}   
    },  
    opset_version=14  # Specify ONNX opset version
)

print("Model successfully converted to ONNX")

# Why convert the PyTorch model to ONNX?
# - When deploying with FastAPI and Docker, using a PyTorch model directly increases the image size significantly.
# - PyTorch dependencies can make the container image bloated, often exceeding several GBs.
# - ONNX provides a lightweight, optimized format that reduces model size and speeds up inference.
# - ONNX models can be used with optimized inference engines like ONNX Runtime, improving performance.
# - This makes the deployment process much more efficient, reducing storage, memory usage, and startup time.
