from huggingface_hub import snapshot_downloader

# settings
user_name = "KIIIIT000"
model_name = "CycleGAN"
repo_id = f"{user_name}/{model_name}"
model_folder = f"models/{model_name}"

# download model from Hugging Face
snapshot_downloader(repo_id, local_dir=model_folder)

print(f"Downloaded {model_name} from Hugging Face: https://huggingface.co/{repo_id}")
