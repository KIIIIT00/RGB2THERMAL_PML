from transformers import AutoModel, AutoTokenizer

# Settings
user_name = "KIIIIT000"
model_name = "CycleGAN"

hugging_model_name = f"{user_name}/{model_name}"

# Load pretrained model and tokenizer
model = AutoTokenizer(model_name, cache_dir=f'models/{model_name}')
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=f'models/{model_name}')

print(f"Save model and tokenizer to {model_name} ... \n")