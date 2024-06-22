from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Initialize the model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_response(query):
    inputs = tokenizer([query], max_length=1024, return_tensors="pt")
    
    with torch.no_grad():
        generated_ids = model.generate(
            inputs["input_ids"],
            max_length=150,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            top_k=50,
            top_p=0.95,
        )
    
    response = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return response

# Test the function
query = "Summarize the importance of artificial intelligence in modern technology."
response = generate_response(query)
print(response)