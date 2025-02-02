from django.test import TestCase

from ..utils import generate_random_8char


class RandomStringTest(TestCase):
    def test_string_length(self):
        result = generate_random_8char()
        self.assertEqual(len(result), 8)

    def test_uniqueness(self):
        """Test that multiple calls produce different strings"""
        results = [generate_random_8char() for _ in range(100)]
        unique_results = set(results)
        self.assertEqual(len(results), len(unique_results))
