# FinTrack

API de controle financeiro pessoal construída com **FastAPI**, **SQLAlchemy**, **PostgreSQL** e **Alembic**.

## Stack

- **FastAPI** — framework HTTP
- **SQLAlchemy 2** — ORM
- **PostgreSQL 16** — banco de dados (via Docker)
- **Alembic** — migrations
- **Pydantic v2 + pydantic-settings** — validação e configuração
- **uvicorn** — servidor ASGI

## Estrutura

```
app/
  core/        # config, database, enums, validators
  models/      # modelos SQLAlchemy (User, Category, Transaction)
  schemas/     # schemas Pydantic
  repositories/# acesso ao banco
  services/    # regras de negócio
  routers/     # endpoints HTTP
  agent/       # (reservado)
  main.py      # entrypoint FastAPI
alembic/       # migrations
```

## Pré-requisitos

- Python 3.12+
- Docker e Docker Compose

## Como rodar

### 1. Clonar e entrar no diretório

```bash
cd fintrack
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz com o seguinte conteúdo:

```env
DATABASE_URL=postgresql://fintrack:fintrack123@localhost:5432/fintrack_db

POSTGRES_USER=fintrack
POSTGRES_PASSWORD=fintrack123
POSTGRES_DB=fintrack_db

APP_ENV=development
APP_DEBUG=true
```

### 5. Subir o banco de dados (Docker)

```bash
docker compose up -d
```

### 6. Rodar as migrations (Alembic)

Aplicar todas as migrations existentes:

```bash
alembic upgrade head
```

### 7. Iniciar o servidor

```bash
uvicorn app.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.
Documentação interativa: `http://127.0.0.1:8000/docs`.

---

## Comandos Alembic úteis

| Ação | Comando |
|---|---|
| Aplicar todas as migrations | `alembic upgrade head` |
| Reverter a última migration | `alembic downgrade -1` |
| Reverter tudo | `alembic downgrade base` |
| Criar nova migration (autogenerate) | `alembic revision --autogenerate -m "descricao"` |
| Ver histórico | `alembic history` |
| Ver migration atual | `alembic current` |

> **Atenção:** sempre rode os comandos alembic com o venv ativado e a partir da raiz do projeto.
