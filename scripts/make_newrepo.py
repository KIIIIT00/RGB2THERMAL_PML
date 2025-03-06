from huggingface_hub import HfApi

# Hugging Face のユーザー名（または組織名）
username = "KIIIT000"  # 変更してください

# 作成するリポジトリ名
repo_name = "RGB2TEHRMAL_DCLGAN"
# リポジトリのフル ID（ユーザー名 + リポジトリ名）
repo_id = f"{username}/{repo_name}"

# 🚀 Hugging Face Hub にリポジトリを作成
api = HfApi()
api.create_repo(repo_id=repo_id, exist_ok=True, private=True)

print(f"Repository created: https://huggingface.co/{repo_id}")