from .server import Response
from .store import STORE


def list_items(req):
    return Response(200, {"items": STORE.all(req.api_key)})


def create_item(req):
    if not isinstance(req.body, dict) or "name" not in req.body:
        return Response(400, {"error": "name is required"})
    item = STORE.create(req.api_key, req.body["name"])
    return Response(201, item)


def get_item(req):
    item_id = req.path.rstrip("/").split("/")[-1]
    item = STORE.get(req.api_key, item_id)
    if item is None:
        return Response(404, {"error": "not found"})
    return Response(200, item)


ROUTES = {
    ("GET", "/v1/items"): list_items,
    ("POST", "/v1/items"): create_item,
    ("GET", "/v1/items/{id}"): get_item,
}
