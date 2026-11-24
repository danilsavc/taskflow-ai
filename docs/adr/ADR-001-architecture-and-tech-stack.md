
# ADR-001: Architecture and Technology Stack

- Status: Accepted
- Date: 2026-11-24

## Context

TaskFlow AI is a full-stack task and project management application.

The project needs an architecture that is:
- Easy to develop and maintain.
- Suitable for an MVP.
- Scalable without unnecessary complexity.
- Clearly separated into frontend and backend.

## Decision

We chose the following architecture and technology stack.

### Architecture

Modular Monolith.

The application will have clearly separated modules and responsibilities, but will run as one backend application.

Microservices are not needed at the current stage.

### Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS

Next.js provides the application framework, React handles UI components, TypeScript adds static typing, and Tailwind CSS is used for styling.

### Backend

- Python 3.12
- FastAPI
- SQLAlchemy (async)
- Alembic
- Pydantic

FastAPI provides the API layer.
SQLAlchemy handles database operations.
Alembic manages database migrations.
Pydantic validates application data.

### Database

- PostgreSQL
- asyncpg

PostgreSQL is used as the primary relational database.
asyncpg provides asynchronous communication with PostgreSQL.

### Infrastructure and Quality

- Docker Compose
- GitHub Actions
- Pytest
- Ruff
- ESLint
- Prettier

Docker Compose manages local development services.
GitHub Actions runs automated checks.
Pytest and Ruff are used for backend testing and code quality.

## Alternatives Considered

### Microservices

Rejected for the initial version because they introduce unnecessary operational complexity.

### SQLite

Not selected as the primary database because the project requires a relational database suitable for multiple users and workspaces.

## Consequences

### Positive

- Clear separation between frontend and backend.
- One backend application is easier to develop and deploy.
- Asynchronous database operations.
- Automated quality checks.
- Architecture can evolve as the project grows.

### Negative

- The backend requires clear module boundaries.
- Developers must maintain separation of responsibilities.
- Async code requires understanding asynchronous programming.

## Future Considerations

The architecture can be extended with additional modules and infrastructure when required.

Possible future components include Redis, background workers, file storage and AI integrations.

These components are not required for the initial foundation.
