# 🚀 FastAPI Message Manager

Este projeto é uma API simples e funcional desenvolvida com **FastAPI** para gerenciar mensagens, utilizando o **PostgreSQL** como banco de dados relacional.

A aplicação permite realizar as operações básicas de CRUD (Criar, Listar e Deletar) de forma rápida e segura.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.11+**
* **FastAPI**: Framework moderno de alta performance.
* **PostgreSQL**: Banco de dados relacional.
* **Psycopg2-binary**: Adaptador de banco de dados para Python.
* **python-dotenv**: Gestão de variáveis de ambiente (.env).
* **Pydantic**: Validação de dados e esquemas.
* **CORS Middleware**: Configuração de segurança para requisições externas.

---

## ⚙️ Instalação e Setup

### 1. Clonar o Repositório

```bash
git clone <seu-repositorio>
cd <nome-do-projeto>
```

### 2. Criar Ambiente Virtual

```bash
# Criar o ambiente
python -m venv venv

# Ativar (Windows)
venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate
```

### 3. Instalar Dependências

```bash
pip install fastapi uvicorn psycopg2-binary python-dotenv pydantic
```

### 4. Configuração do Banco de Dados

No seu PostgreSQL, crie o banco de dados:

```sql
CREATE DATABASE meu_projeto;
```

Crie um arquivo chamado `.env` na raiz do projeto e configure a URL de conexão:

```
DATABASE_URL=postgresql://usuario:senha@localhost:5432/meu_projeto
```

> Substitua `usuario` e `senha` pelas suas credenciais reais do Postgres.

### 5. Executar a Aplicação

Para rodar a aplicação em modo de desenvolvimento:

```bash
uvicorn main:app --reload
```

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 6. Documentação Automática

O FastAPI fornece interfaces visuais para testar a API sem precisar de ferramentas externas:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🛣️ Endpoints da API

| Método | Endpoint        | Descrição                               |
| ------ | --------------- | --------------------------------------- |
| GET    | /mensagens      | Lista todas as mensagens do banco.      |
| POST   | /mensagens      | Cadastra uma nova mensagem.             |
| DELETE | /mensagens/{id} | Remove uma mensagem específica pelo ID. |

### Exemplo de JSON para POST

```json
{
  "conteudo": "Minha primeira mensagem!"
}
```

---

## 📝 Notas

* Certifique-se de
