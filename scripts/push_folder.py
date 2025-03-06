from huggingface_hub import HfApi

repo_name = "RGB2TEHRMAL_CycleGAN"
username = "KIIIT000"
repo_id = f"{username}/{repo_name}"

model_folder_name = "rgbtothermal_cyclegan"
upload_folder_path = f"CycleGAN/checkpoints/{model_folder_name}"
repo_subfolder = f"checkpoints/{model_folder_name}"

api = HfApi()
api.upload_folder(
    folder_path=upload_folder_path,
    repo_id=repo_id,
    repo_type="model",
    path_in_repo=repo_subfolder,
)

print(f"✅ Uploaded {upload_folder_path} to Hugging Face: https://huggingface.co/{repo_id}/tree/main/{repo_subfolder}")