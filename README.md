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
1. `pip3 install python-dotenv`

### 設定

.env.exampleを参考に、.envを作成

例)
```
$ vi .env
QRZ_USER=jq3juk
QRZ_PASS=パスワード
```

### 入力ファイル作成

テキストファイルに1行1コールサインで列挙

例)
```
$ cat callsigns.txt
JQ3JUK
JA1RL
8K3EXPO
```

### 実行

引数に渡したファイルに拡張子`.csv`を付けたファイルにCSV形式で出力されます。
1行目はヘッダ行です。差し込み印刷時の参考にして下さい。

```
$ python3 ./callsign_to_address.py callsigns.txt
$ cat callsigns.txt.csv
callsign,name,addr1,addr2,state,zipcode,country
JQ3JUK,Masatoshi Kamagasako,番地,"Nishi-ku, Kobe-city, Hyogo",,651-xxxx,JAPAN
JA1RL,JARL (Central Station - CHUOKYOKU) Japan Amateur Radio League,,Toshima Tokyo,,,JAPAN
8K3EXPO,"Japan Amateur Radio League Special Amateur Radio Station For Expo 2025 Osaka, Kansai, Japan",,Osaka,,,JAPAN
```

## 注意事項

出力されたCSVに記載された住所が適切か、事前に確認して下さい。

- 上の実行例のように、qrz.comに設定されている住所をそのまま取得します。ユーザによっては不達となる住所が設定されている可能性があります。
- 国名(country)カラムにDXCCエンティティ名が設定されていることがあるようです。
- QSLマネージャが設定されていることがあります。
- SASE/SAE送付先がqrz.comの本文に記載されていることがあります。

## ToDo

- エラーハンドリング
- ~~ID/passwordの外部化~~
- QSL Managerが設定されている場合の処理
