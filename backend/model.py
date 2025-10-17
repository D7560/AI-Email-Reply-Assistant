from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

def load_model(model_name: str = "google/flan-t5-small"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    model.eval()
    return model, tokenizer

def generate_reply(model, tokenizer, prompt: str, max_tokens: int = 80):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
    device = next(model.parameters()).device
    inputs = {k: v.to(device) for k, v in inputs.items()}
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=max_tokens, do_sample=True, top_p=0.9, temperature=0.8)
    return tokenizer.decode(out[0], skip_special_tokens=True).strip()
