# python-ce

> pythonをホストで実行するためのdocker環境です

## Usage
```
docker-compose build (初回のみ実行)
```
```
docker compose up -d
docker exec -it python-app sh
```
コンテナーにログイン（#が表示） 

次を（Python）コマンドします
```
python <実行したいファイル名>
```

サンプルとして以下をお試しください
```
python getaddress_otaru.py
```
```
python getaddress_minatoku.py
```
 
---

> See [Wiki](https://github.com/watanabe3tipapa/python-ce/wiki) for more details

---
> This repository is for a workshop I will be attending.
  
^C
