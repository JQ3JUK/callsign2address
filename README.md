# callsign2address
fetch address from qrz.com by callsign

コールサインをもとにqrz.comから該当する局の住所を取得し、CSVに出力します。
出力したCSVはラベル屋さんに読み込ませてラベルシールに印刷できます。

## 必要なもの

- qrz.comの[XML Log Data Subscription](https://shop.qrz.com/collections/subscriptions/products/xml-logbook-data-subscription-1-year)
- Python3実行環境

## 使い方

### 下準備

1. ローカルに`git clone`
1. `python3 -m venv venv`
1. `. venv/bin/activate`
1. `pip3 install requests`

### 入力ファイル作成

テキストファイルに1行1コールサインで列挙

### 実行

```python3 ./callsign_to_address.py callsigns.csv```

## ToDo

- QSL Managerが設定されている場合の処理
