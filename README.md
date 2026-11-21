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
- SQLAlchemy
- Alembic
- PostgreSQL
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
│   └── tests/
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

Create a `.env` file inside `backend/` using `.env.example` as a template.

Install backend dependencies:

```bash
python -m venv .venv
```

Activate the virtual environment and install the required Python packages.

### 4. Run database migrations

From the `backend/` directory:

```bash
alembic upgrade head
```

### 5. Start the backend

From the `backend/` directory:

```bash
python -m uvicorn app.main:app --reload
```

Backend URLs:

- API: http://127.0.0.1:8000
- Swagger documentation: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health
- Database readiness: http://127.0.0.1:8000/ready

### 6. Configure and start the frontend

From the `frontend/` directory:

```bash
npm install
npm run dev
```

Frontend URL: http://localhost:3000

## Quality Checks

### Backend

```bash
ruff check backend/
python -m pytest -v
```

### Frontend

```bash
npm run lint
npx prettier --check .
```

## Continuous Integration

GitHub Actions automatically runs backend and frontend checks on every push and pull request.

## Project Status

Currently implemented:
- Initial project structure
- FastAPI backend
- PostgreSQL database
- SQLAlchemy and Ale