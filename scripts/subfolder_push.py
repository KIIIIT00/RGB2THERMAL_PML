import os
from tqdm import tqdm
from huggingface_hub import HfApi

# Hugging Faceのリポジトリ情報
USER_NAME = "KIIIT000"
MODEL_FOLDER = "models"

# Hugging Face API インスタンス
api = HfApi()
for model_name in tqdm(os.listdir(MODEL_FOLDER)):
    print(f"----------------- {model_name} push start -----------------")
    if model_name =='.gitkeep':
        continue
    repo_name = f"RGB2TEHRMAL_{model_name}"
    repo_id = f"{USER_NAME}/{repo_name}"
    base_folder = os.path.join(MODEL_FOLDER, model_name)
    if model_name == 'MUNIT':
        base_folder = os.path.join(base_folder, 'outputs')

    # Hugging Face APIインスタンス
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
    
    print(f"----------------- {model_name} has been uploaded successfully! -----------------")
    
print("All Models subfolders in `checkpoints/` have been uploaded successfully!")