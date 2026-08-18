import itertools
import threading


class Store:
    def __init__(self):
        self._items = {}
        self._ids = itertools.count(1)
        self._lock = threading.Lock()

    def all(self, key):
        with self._lock:
            return list(self._items.get(key, {}).values())

    def create(self, key, name):
        with self._lock:
            item_id = str(next(self._ids))
            item = {"id": item_id, "name": name}
            self._items.setdefault(key, {})[item_id] = item
            return item

    def get(self, key, item_id):
        with self._lock:
            return self._items.get(key, {}).get(item_id)


STORE = Store()
