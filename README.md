# python-ce

> pythonをホストで実行するためのdocker環境です

## Usage
```
docker-compose build (初回のみ実行)
docker-compose up -d
docker exec -it python-app sh
python <実行したいファイル名>
```

サンプルとして以下をお試しください
```
python getaddress_otaru.py
```
```
python getaddress_minatoku.py
```

^C
