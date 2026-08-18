import random

from cache import ttl_cache


class BackendUnavailable(Exception):
    pass


def _http_get_user(user_id):
    # Stand-in for the real HTTP client. Flaps under load.
    if random.random() < 0.3:
        raise BackendUnavailable("upstream 503")
    return {"id": user_id, "name": "user-%s" % user_id, "plan": "pro"}


@ttl_cache(30)
def get_user(user_id):
    return _http_get_user(user_id)


def get_user_plan(user_id):
    return get_user(user_id)["plan"]
