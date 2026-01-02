# 🌌 X-PRIVE API | FastAPI Backend

A **X-PRIVE API** é uma API de alta performance que sustenta o ecossistema X-PRIVE, responsável pela persistência de dados no **PostgreSQL** e pelo gerenciamento dos portais de atalho.

---

## 🛠️ Requisitos

Para rodar a API, você precisará de:

* Python 3.9 ou superior
* PostgreSQL (local ou remoto, como Supabase ou Render)
* Pip (gerenciador de pacotes do Python)

---

## 📦 Instalação

1. Clone o repositório e entre na pasta da API:

```bash
git clone <seu-repositorio>
cd x-prive-api
```

2. Instale as dependências necessárias:

```bash
pip install fastapi uvicorn psycopg2-binary python-dotenv
```

3. Configure as variáveis de ambiente criando um arquivo `.env` na raiz do projeto:

```
DATABASE_URL=postgres://usuario:senha@localhost:5432/nome_do_banco
```

> Substitua `usuario`, `senha` e `nome_do_banco` pelos dados do seu PostgreSQL.

---

## 🚀 Executando o Servidor

Inicie a API usando Uvicorn com hot reload ativo:

```bash
uvicorn main:app --reload
```

A API estará disponível em: [http://localhost:8000](http://localhost:8000)

---

## 📑 Documentação Automática

O FastAPI gera documentação interativa automaticamente:

* **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
* **Redoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🛣️ Endpoints Disponíveis

| Método | Endpoint    | Descrição                                  |
| ------ | ----------- | ------------------------------------------ |
| GET    | /sites      | Lista todos os atalhos salvos no banco.    |
| POST   | /sites      | Adiciona um novo portal (JSON: name e url) |
| DELETE | /sites/{id} | Remove um portal permanentemente pelo ID   |

### Exemplo de JSON para POST

```json
{
  "name": "Site Exemplo",
  "url": "https://exemplo.com"
}
```

---

## 🗄️ Estrutura do Banco de Dados

A tabela `sites` é criada automaticamente no startup da API:

| Campo | Tipo   | Descrição            |
| ----- | ------ | -------------------- |
| id    | SERIAL | Chave primária       |
| name  | TEXT   | Nome do site         |
| url   | TEXT   | URL completa do site |

---

## ⚠️ Observações de Segurança

* Configure o CORS no `main.py` para permitir apenas o domínio do front-end em produção.
* Mantenha o arquivo `.env` seguro e **nunca versionado** no Git.
