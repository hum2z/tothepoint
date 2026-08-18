# keyapi

Small internal API. All requests carry `X-Api-Key`.

## Endpoints

| Method | Path | Auth | Responses |
|---|---|---|---|
| GET | `/v1/items` | api key | 200, 401 |
| POST | `/v1/items` | api key | 201, 400, 401 |
| GET | `/v1/items/{id}` | api key | 200, 401, 404 |

## Middleware chain

Declared in `app/server.py`. Order matters: request logging runs first so that
rejected requests still show up in the access log.
