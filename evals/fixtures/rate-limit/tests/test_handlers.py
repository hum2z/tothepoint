import unittest

from app.handlers import ROUTES
from app.server import MIDDLEWARE, App, Request


def make_app():
    return App(ROUTES, MIDDLEWARE)


class TestHandlers(unittest.TestCase):
    def setUp(self):
        self.app = make_app()
        self.headers = {"X-Api-Key": "k_test"}

    def test_requires_api_key(self):
        resp = self.app.handle(Request("GET", "/v1/items"))
        self.assertEqual(resp.status, 401)

    def test_create_and_list(self):
        self.app.handle(Request("POST", "/v1/items", self.headers, {"name": "a"}))
        resp = self.app.handle(Request("GET", "/v1/items", self.headers))
        self.assertEqual(resp.status, 200)
        self.assertEqual(len(resp.body["items"]), 1)

    def test_create_validates(self):
        resp = self.app.handle(Request("POST", "/v1/items", self.headers, {}))
        self.assertEqual(resp.status, 400)


if __name__ == "__main__":
    unittest.main()
