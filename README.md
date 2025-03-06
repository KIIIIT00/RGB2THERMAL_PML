# RGB2THERMAL_PML
このリポジトリには，Hugging Faceにアップロードした学習したモデルとHugging Faceへのアップロードするファイルが存在する．
以下に，モデルの詳細や利用方法を記載している．

## モデル一覧
Hugging Face上のモデルは以下のリンクからアクセスできる．
### 1.[CycleGAN](https://huggingface.co/KIIIT000/RGB2TEHRMAL_CycleGAN)
### 2.[CSTGAN](https://huggingface.co/KIIIT000/RGB2TEHRMAL_CSTGAN)
### 3.[DCLGAN](https://huggingface.co/KIIIT000/RGB2TEHRMAL_DCLGAN)
### 4.[MUNIT](https://huggingface.co/KIIIT000/RGB2TEHRMAL_MUNIT)

## モデルの利用方法
Hugging Faceからアップロードしたモデルをローカル環境にダウンロードする方法
## 1.Gitを使用してリポジトリをローカルにクローンする
### 必要なツール:
- **Git**:([Git公式サイト](https://git-scm.com/)からインストール)

### 手順:
1.**Git LFSのインストール**(必要な場合)
Hugging Faceでは，大きなファイル(例えばモデルの重み)をGit LFS(Git Large File Storage)で管理する場合がある．
まず，Git LFSをインストールする．

``` bash
git lfs install
```
2.**リポジトリをクローン**
``` bash
git clone https://huggingface.co/username/model_name
```
## 2.transformersライブラリを使う方法
transformersライブラリを使ってモデルをローカルにダウンロードすることができる．この方法では，Hugging Faceのモデルリポジトリから直接モデルを読みこみ，ローカルに保存する．
### 必要なツール:
- **transformers**ライブラリ

### 手順
1.**transformersをインストール**

``` bash
pip install transformers
```
2.**ファイルを実行**


## 3.huggingface_hubライブラリを使う方法
huggingface_hubライブラリを使って、Hugging Faceから直接リポジトリをダウンロードすることができる．この方法では、指定したファイルを直接ローカルに保存できる．
### 必要なツール:
- **huggingface_hub**ライブラリ

### 手順
1.**huggingface_hubをインストール**
```bash
pip install huggingface_hub
```

