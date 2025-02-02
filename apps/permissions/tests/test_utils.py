from django.test import TestCase

from ..utils import generate_token


class TokenTest(TestCase):
    def test_token_length(self):
        result = generate_token()
        self.assertEqual(len(result), 36)

    def test_uniqueness(self):
        results = [generate_token() for _ in range(100)]
        unique_results = set(results)
        self.assertEqual(len(results), len(unique_results))
