import os
from huggingface_hub import HfApi

# Hugging Faceのリポジトリ情報
model_name = "CycleGAN"
user_name = "KIIIT000"
repo_name = f"RGB2TEHRMAL_{model_name}"
repo_id = f"{user_name}/{repo_name}"
base_folder = f"models/{model_name}"

# Hugging Face API インスタンス
api = HfApi()

for subfolder in os.listdir(base_folder):
    full_path = os.path.join(base_folder, subfolder)
    
    if os.path.isdir(full_path):
        print(f"Uploading {full_path} to Hugging Face ... \n")
        
        api.upload_folder(
            folder_path=full_path,
            repo_id=repo_id,
            repo_type="model",
            path_in_repo=f"checkpoints/{subfolder}",
        )
        
        print(f"Uploaded {full_path} to Hugging Face: https://huggingface.co/{repo_id}/tree/main/{full_path}")

print("All subfolders in `checkpoints/` have been uploaded successfully!")