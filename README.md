# 概要
ASGI web サーバーであるHypercornを使って、WSGIである Django2を動かすためのリポジトリ  
for PyCon mini Hiroshima  
[Pycon mini Hiroshima](https://hiroshima.pycon.jp/2020/speaker/JunyaFff)  

Python 3.8.1 を利用

# オレオレな鍵を作る

```
brew install mkcert
mkcert -install
mkcert example.com  localhost 127.0.0.1 ::1
```

ファイルができているのをご確認ください。
* example.com+3-key.pem
* example.com+3.pem

それぞれrenameしてください。

 * example.com+3-key.pem  → key.pem
 * example.com+3.pem → cert.pem


# Usage 

```
pip install hypercorn
pip install django==2.2.16
```

HTTP2での動作させる場合  
```
hypercorn --config=h2_config.py httptest.asgi:asyncio_app
```

HTTP/1.1で動作させる場合
```
hypercorn --config=h11_config.py httptest.asgi:asyncio_app
```


