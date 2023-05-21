# App Caronas

- [Instalação](#instalação)
- [API](#api)

***

## Instalação

* Cria uma pasta. Ex: `app-fat`.
* Baixe os arquivos repositório. Ex: `git clone https://github.com/UERJ-LIVIA/app-fat-carona`.
* Crie um ambiente virtual: `python3 -m venv env` (ou `python -m venv env`).
* Ative o ambiente virtual: `source env/bin/activate`.
* Entre na pasta do repositório. Ex: `cd app-fat-carona`.
* Instale as dependências: `pip install -r requirements.txt`.
* Inicie o site: `python manage.py runserver 8000`.

***

## API

### Exemplo

`GET /api/example/` - Criar um objeto de exemplo.

| Parâmetro | Tipo |
|-|-|
| text | String |
| pubdate | Date "YYYY-MM-DD" (na ausência) |

Exemplo de envio:
  ```
    {
        "text": "Teste",
    }
  ```

`POST /api/example/` - Recuperar todos os objetos de exemplo. Não precisa de argumentos.