"""Tiny WSGI-ish app. No third-party deps on purpose."""
import json
import logging

log = logging.getLogger("keyapi")


class Request:
    def __init__(self, method, path, headers=None, body=None):
        self.method = method
        self.path = path
        self.headers = headers or {}
        self.body = body


class Response:
    def __init__(self, status, body=None, headers=None):
        self.status = status
        self.body = body
        self.headers = headers or {}

    def to_json(self):
        return json.dumps({"status": self.status, "body": self.body})


def logging_middleware(req, nxt):
    log.info("%s %s", req.method, req.path)
    resp = nxt(req)
    log.info("-> %s", resp.status)
    return resp


def auth_middleware(req, nxt):
    key = req.headers.get("X-Api-Key")
    if not key:
        return Response(401, {"error": "missing api key"})
    if not key.startswith("k_"):
        return Response(401, {"error": "invalid api key"})
    req.api_key = key
    return nxt(req)


class App:
    def __init__(self, routes, middleware):
        self.routes = routes
        self.middleware = middleware

    def handle(self, req):
        def dispatch(r):
            handler = self.routes.get((r.method, _template(r.path)))
            if handler is None:
                return Response(404, {"error": "not found"})
            return handler(r)

        chain = dispatch
        for mw in reversed(self.middleware):
            chain = _wrap(mw, chain)
        return chain(req)


def _wrap(mw, nxt):
    return lambda r: mw(r, nxt)


def _template(path):
    parts = path.strip("/").split("/")
    if len(parts) == 3 and parts[0] == "v1":
        return "/v1/items/{id}"
    return "/" + "/".join(parts)


MIDDLEWARE = [logging_middleware, auth_middleware]
