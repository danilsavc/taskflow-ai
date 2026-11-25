# ADR-002: Authentication and Session Strategy

- Status: Accepted
- Date: 2026-11-25

## Context

TaskFlow AI needs an authentication system that allows users to register, log in, access protected resources, and log out.

The system must:
- Protect user accounts and private data.
- Store passwords securely.
- Support authenticated API requests.
- Work with a separate Next.js frontend and FastAPI backend.

## Decision

We chose JWT-based authentication with an HttpOnly Cookie.

### Password Storage

- Passwords are hashed using Argon2.
- Plain-text passwords are never stored in the database.
- Password verification is performed using the stored password hash.

### Authentication Token

- JWT is used as the access token.
- Tokens are signed using HS256.
- The token contains the user ID in the `sub` claim.
- The token expiration time is 30 minutes.

### Session Storage

The JWT is stored in an HttpOnly Cookie.

Cookie settings:
- `HttpOnly`: true
- `Secure`: false in local development; true in production over HTTPS.
- `SameSite`: Lax
- `Max-Age`: 30 minutes
- `Path`: /

The frontend sends cookies with authenticated requests using `credentials: "include"`.

### Logout

Logout removes the authentication cookie from the browser.

The JWT itself is not revoked server-side. It remains cryptographically valid until expiration, but the browser no longer sends it after the cookie is deleted.

### Authorization

A shared FastAPI dependency called `get_current_user`:
1. Reads the access token from the cookie.
2. Verifies the JWT.
3. Retrieves the user from the database.
4. Returns the authenticated user or raises HTTP 401.

## Alternatives Considered

### Server-side Sessions

Rejected for the initial version because they require session storage and additional session management.

### JWT in Local Storage

Rejected because JavaScript can access local storage, increasing the risk of token theft through XSS attacks.

## Consequences

### Positive
- Passwords are stored securely as hashes.
- HttpOnly Cookie prevents JavaScript from directly reading the token.
- JWT validation does not require a separate session lookup.
- Authentication logic is separated into reusable dependencies and services.

### Negative
- JWT cannot be immediately revoked without additional server-side mechanisms.
- Cookie-based authentication requires consideration of CSRF protection.
- Token expiration must be handled by the frontend.

## Security Considerations

- HTTPS must be enabled in production.
- The `Secure` cookie flag must be enabled in production.
- CSRF protection must be evaluated before production deployment.
- JWT secret keys must be stored in environment variables and never committed to Git.

## Future Considerations

Possible improvements:
- Refresh token mechanism.
- Server-side token revocation.
- CSRF protection.
- Rate limiting for authentication endpoints.
