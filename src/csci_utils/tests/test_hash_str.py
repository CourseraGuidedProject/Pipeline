
"""Tests for hash_str module."""

import os
from tempfile import TemporaryDirectory
from unittest import TestCase


from csci_utils.hash_str import hash_str


class HashTests(TestCase):
    def test_basic(self):
        # The result is from https://md5calc.com/hash/sha256/John+Doe%0D%0A
        self.assertEqual(hash_str("John", salt=" Doe").hex()[:6], "ec9a41")
        self.assertEqual(hash_str("world!", salt="hello, ").hex()[:6], "68e656")
    
    def test_empty_string(self):
        # The result is from the above site.
        self.assertEqual(hash_str("",salt="").hex()[:6], "e3b0c4")
    
    def test_invalid_input(self):
        """Ensure invalid input will raise the correct Exception"""
        self.assertRaises(TypeError, hash_str,3.14)
        



