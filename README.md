# Decopon 🍊

これは、2023年度の創造実験用のプログラムです。

Getting Started (学科計算機)
===============

このコードをコピーして、ディレクトリに移動します。
```
git clone https://github.com/matt76k/decopon
cd decopon
```

decoponを使えるようにするため、必要なライブラリをインストールします。
```
pip install pygame pymunk
```

ゲームを起動しましょう。
```
PYTHONPATH=$PWD python3 src/main.py
```

Getting Started (通常)
===============

poetryをインストールします。
[poetry](https://python-poetry.org/docs/)のページを参考に、自分の環境に合った方法でインストールしてください。

```
curl -sSL https://install.python-poetry.org | python -
```

decoponを使えるようにするため、installします。

```
poetry install
```

installできたら、ゲームを起動しましょう。

```
poetry run python src/main.py
```

Develop
===============
main.pyの最後にRandomPlayerがあるので、それを参考にPlayerを実装しましょう。