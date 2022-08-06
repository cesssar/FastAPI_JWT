# FastAPI com JWT 🚀

**Esqueleto básico de API em Python com FastAPI e autenticação JWT**

## Requisitos

- Python 3.6+
- FastAPI
- PyJWT

Recomenda-se criar um ambiente isolado para instalar as dependências (<a href="https://docs.python.org/3/library/venv.html">venv</a>)

```console
$ pip install -r requirements.txt

```
Criar um arquivo .env na pasta app com seguintes chaves

secret_key=c3544c754bec26d5235dcb1c47668388a995f347036a1d66
algorithm=HS256

Para gerar uma nova secret_key, execute os comandos abaixo no console do Python

```console
>>> import os
>>> import binascii
>>> binascii.hexlify(os.urandom(24))
b'deff1952d59f883ece260e8683fed21ab0ad9a53323eca4f'

```

## Executar

```console
$ python main.py
```

Créditos: <a href="https://testdriven.io/blog/fastapi-jwt-auth/">Abdulazeez Abdulazeez Adeshina</a>
