from http import HTTPStatus

from django.test import Client, TestCase
import parameterized


class StaticURlTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)


class StaticURL(TestCase):
    @parameterized.parameterized.expand(
        [
            ("0", HTTPStatus.OK),
            ("1", HTTPStatus.OK),
            ("01", HTTPStatus.OK),
            ("010", HTTPStatus.OK),
            ("10", HTTPStatus.OK),
            ("100", HTTPStatus.OK),
            ("abcd", HTTPStatus.NOT_FOUND),
            ("aa4a", HTTPStatus.NOT_FOUND),
            ("232%", HTTPStatus.NOT_FOUND),
            ("-0", HTTPStatus.NOT_FOUND),
            ("-1", HTTPStatus.NOT_FOUND),
        ]
    )
    def test_catalog_kik(self, kik, expected_status):
        status_code = Client().get(f"/catalog/{kik}/").status_code
        self.assertEqual(
            status_code,
            expected_status,
            msg=f"/catalog/{kik}/ get not {expected_status}",
        )


class StaticURLTest(TestCase):
    @parameterized.parameterized.expand(
        [
            ("0", HTTPStatus.NOT_FOUND),
            ("1", HTTPStatus.OK),
            ("01", HTTPStatus.NOT_FOUND),
            ("010", HTTPStatus.NOT_FOUND),
            ("10", HTTPStatus.OK),
            ("100", HTTPStatus.OK),
            ("abcd", HTTPStatus.NOT_FOUND),
            ("aa4a", HTTPStatus.NOT_FOUND),
            ("232%", HTTPStatus.NOT_FOUND),
            ("-0", HTTPStatus.NOT_FOUND),
            ("-1", HTTPStatus.NOT_FOUND),
        ]
    )
    def test_catalog_kio(self, kio, expected_status):
        status_code = Client().get(f"/catalog/re/{kio}/").status_code
        self.assertEqual(
            status_code,
            expected_status,
            msg=f"/catalog/re/{kio}/ get not {expected_status}",
        )


class StaticUrlTest(TestCase):
    @parameterized.parameterized.expand(
        [
            ("0", HTTPStatus.NOT_FOUND),
            ("1", HTTPStatus.OK),
            ("01", HTTPStatus.NOT_FOUND),
            ("010", HTTPStatus.NOT_FOUND),
            ("10", HTTPStatus.OK),
            ("100", HTTPStatus.OK),
            ("abcd", HTTPStatus.NOT_FOUND),
            ("aa4a", HTTPStatus.NOT_FOUND),
            ("232%", HTTPStatus.NOT_FOUND),
            ("-0", HTTPStatus.NOT_FOUND),
            ("-1", HTTPStatus.NOT_FOUND),
        ]
    )
    def test_catalog_kill(self, kill, expected_status):
        status_code = Client().get(f"/catalog/converter/{kill}/").status_code

        self.assertEqual(
            status_code,
            expected_status,
            msg=f"/catalog/converter/{kill}/ get not {expected_status}",
        )
