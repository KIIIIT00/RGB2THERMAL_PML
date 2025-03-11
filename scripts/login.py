import os
from huggingface_hub import login
from dotenv import load_dotenv

load_dotenv()

hf_token = os.getenv("HUGGINGFACE_TOKEN")
if hf_token:
    login(token=hf_token)
    print("Hugging Face にログインしました")
else:
    print("HUGGINGFACE_TOKEN が設定されていません")