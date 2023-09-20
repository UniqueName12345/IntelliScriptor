import torch
from transformers import pipeline

text_generation = pipeline(model="PY007/TinyLlama-1.1B-step-50K-105b", torch_dtype=torch.bfloat16, device_map="auto")

def continue_text_generation(text):
    return text_generation(text)