
# TaskFlow AI

TaskFlow AI is a full-stack task and project management application.

## Tech Stack

### Frontend
- Next.js
- React
- TypeScript
- Tailwind CSS
- ESLint
- Prettier

### Backend
- Python 3.12
- FastAPI
- SQLAlchemy (async)
- Alembic
- PostgreSQL
- asyncpg
- Pydantic
- Ruff
- Pytest

### Infrastructure
- Docker Compose
- GitHub Actions

## Project Structure

```text
taskflow-ai/
├── .github/
│   └── workflows/
├── backend/
│   ├── app/
│   ├── migration/
│   ├── tests/
│   ├── .env.example
│   ├── requirements.txt
│   └── alembic.ini
├── frontend/
├── docs/
│   └── diagrams/
├── docker-compose.yml
└── README.md
```

## Prerequisites

Install the following tools:

- Python 3.12
- Node.js 22
- npm
- Docker Desktop
- Git

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/danilsavc/taskflow-ai
cd taskflow-ai
```

### 2. Start PostgreSQL

```bash
docker compose up -d
```

### 3. Configure the backend

From the project root, create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install backend dependencies:

```powershell
pip install -r backend/requirements.txt
```

Create a `.env` file inside `backend/` using `.env.example` as a template.

### 4. Run database migrations

From the `backend/` directory:

```powershell
python -m alembic upgrade head
```

### 5. Start the backend

From the `backend/` directory:

```powershell
python -m uvicorn app.main:app --reload
```

Backend URLs:

- API: http://localhost:8000
- Swagger documentation: http://localhost:8000/docs
- Health check: http://localhost:8000/health
- Database readiness: http://localhost:8000/ready

### 6. Configure and start the frontend

From the `frontend/` directory:

```bash
npm install
npm run dev
```

Frontend URL: http://localhost:3000

## Quality Checks

### Backend

From the project root:

```powershell
ruff check backend/
```

From the `backend/` directory:

```powershell
python -m pytest -v
```

### Frontend

From the `frontend/` directory:

```bash
npm run lint
npx prettier --check .
npm run build
```

## Continuous Integration

GitHub Actions automatically runs backend and frontend checks on every push and pull request.

## Project Status

Currently implemented:

- Initial project structure
- FastAPI backend
- PostgreSQL database connection
- Asynchronous SQLAlchemy engine and sessions
- Alembic database migrations
- User registration schemas
- Password hashing and verification
- Health and database readiness endpoints
- Backend tests
- Ruff code quality checks
- Frontend application setup
- GitHub Actions CI workflow
