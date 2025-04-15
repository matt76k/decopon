# Decopon 🍊

## 実験の準備

1. まずRyeをインストールします。OSに応じて以下のコマンドを実行してください:

Linux/macOSの場合:
```bash
curl -sSf https://rye.astral.sh/get | bash
```

Windowsの場合:
- [Ryeのインストールページ](https://rye.astral.sh/guide/installation/)から適切なバイナリをダウンロード
- ダウンロードしたファイルを実行

2. リポジトリをクローンし、必要なライブラリをインストール:
```bash
git clone https://github.com/matt76k/decopon/
cd decopon
rye sync
```

3. 実行
```
rye run python src/main.py
```

Develop
===============
main.pyの最後にRandomPlayerがあるので、それを参考にPlayerを実装しましょう。