from http import HTTPStatus

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_coffee(self):
        response = Client().get("/coffee/")
        self.assertEqual(response.status_code, 418)
