#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Luigi target module."""
import os

from unittest import TestCase
from ..luigi.target import SuffixPreservingLocalTarget


class TestTarget(TestCase):
    def test_temp_file(self):
        temp_file = "test.abcd"
        suffix_target = SuffixPreservingLocalTarget(temp_file)
        with suffix_target.temporary_path() as f:
            self.assertTrue(suffix_target.open(mode="w").name.endswith(".abcd"))
        #clean up
        os.remove(temp_file)


