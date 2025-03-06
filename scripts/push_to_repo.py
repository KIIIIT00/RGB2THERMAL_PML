from huggingface_hub import HfApi

repo_id = "KIIIT000/RGB2THERMAL_PML"
folder_path = "./CycleGAN/checkpoints/rgbtothermal_cyclegan" # appload foldername
branch_name = 'add-CycleGAN'
commit_msg = "[add] CycleGAN rgbtothermal_cyclegan"  # コミットメッセージ

# リポジトリを作成
api = HfApi()
api.create_repo(repo_id=repo_id, exist_ok=True, private=True)
print(f"Repository created: https://huggingface.co/{repo_id}")


# フォルダごとアップロード（ブランチ指定）
api.upload_folder(
    folder_path=folder_path,
    repo_id=repo_id,
    repo_type="model",
    revision=branch_name  # ここでブランチを指定
)

