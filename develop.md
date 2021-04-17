# テストページ

This is a test page. Never mind.

<!-- textlint-disable ja-technical-writing/no-mix-dearu-desumasu -->

これはテスト用のページであり、ノートブックの内容は公開前に変更されることがあります。

<!-- textlint-enable -->

## ノートブック

1. [高機能な電卓](https://nbviewer.jupyter.org/github/tueda/PS2021SS/blob/develop/notebooks/01_%E9%AB%98%E6%A9%9F%E8%83%BD%E3%81%AA%E9%9B%BB%E5%8D%93.ipynb) [![Download ipynb](https://img.shields.io/badge/download-ipynb-brightgreen.svg?logo=jupyter)](https://raw.githubusercontent.com/tueda/PS2021SS/develop/notebooks/01_%E9%AB%98%E6%A9%9F%E8%83%BD%E3%81%AA%E9%9B%BB%E5%8D%93.ipynb) [![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tueda/PS2021SS/develop?filepath=notebooks/01_%E9%AB%98%E6%A9%9F%E8%83%BD%E3%81%AA%E9%9B%BB%E5%8D%93.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tueda/PS2021SS/blob/develop/notebooks/01_%E9%AB%98%E6%A9%9F%E8%83%BD%E3%81%AA%E9%9B%BB%E5%8D%93.ipynb?hl=ja)
1. [条件分岐](https://nbviewer.jupyter.org/github/tueda/PS2021SS/blob/develop/notebooks/02_%E6%9D%A1%E4%BB%B6%E5%88%86%E5%B2%90.ipynb) [![Download ipynb](https://img.shields.io/badge/download-ipynb-brightgreen.svg?logo=jupyter)](https://raw.githubusercontent.com/tueda/PS2021SS/develop/notebooks/02_%E6%9D%A1%E4%BB%B6%E5%88%86%E5%B2%90.ipynb) [![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tueda/PS2021SS/develop?filepath=notebooks/02_%E6%9D%A1%E4%BB%B6%E5%88%86%E5%B2%90.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tueda/PS2021SS/blob/develop/notebooks/02_%E6%9D%A1%E4%BB%B6%E5%88%86%E5%B2%90.ipynb?hl=ja)
1. 反復処理
1. 関数
1. グラフの描画
1. 文字列処理
1. 乱数
1. モンテカルロ法
1. ランダムウォーク
1. フラクタル
1. セルオートマトン
1. 方程式の解
1. 運動のシミュレーション
1. まとめ演習

- [動作確認](https://nbviewer.jupyter.org/github/tueda/PS2021SS/blob/develop/notebooks/00_%E5%8B%95%E4%BD%9C%E7%A2%BA%E8%AA%8D.ipynb) [![Download ipynb](https://img.shields.io/badge/download-ipynb-brightgreen.svg?logo=jupyter)](https://raw.githubusercontent.com/tueda/PS2021SS/develop/notebooks/00_%E5%8B%95%E4%BD%9C%E7%A2%BA%E8%AA%8D.ipynb) [![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tueda/PS2021SS/develop?filepath=notebooks/00_%E5%8B%95%E4%BD%9C%E7%A2%BA%E8%AA%8D.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tueda/PS2021SS/blob/develop/notebooks/00_%E5%8B%95%E4%BD%9C%E7%A2%BA%E8%AA%8D.ipynb?hl=ja)


## Development

We still use 3.6, though recently Google Colaboratory and MyBinder have switched to 3.7.
```
# on Ubuntu 20.04
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6  # 3.6.13 as of 18 March 2021

poetry env use python3.6
poetry install
poetry run task setup
```


## Branches

- master: dummy text
- develop: general development, including temporary versions
- stable: source for deployment
- gh-pages: deployment
