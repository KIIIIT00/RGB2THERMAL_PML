# ベースイメージとしてPython 3.12を使用
FROM python:3.12-slim

# 環境変数設定
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを設定
WORKDIR /workspace

# requirements.txt をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# .envファイルの読み込み用にpython-dotenvを追加
RUN pip install --no-cache-dir python-dotenv huggingface_hub

# コンテナ起動時に bash を使用可能にする
CMD ["bash"]
