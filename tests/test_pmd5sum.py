import pytest
import unittest
import pmd5sum
import os

class TestGitui(unittest.TestCase):

    def test_pmd5sum(self):
        path = get_fixture_path('foo.txt')
        assert pmd5sum.md5(path) == '08f1edfc5248e764a7f1cf00a58b3a6e'

        with(pytest.raises(IOError)):
            pmd5sum.md5('santehounasuhoe')


def get_fixture_path(*args):
    return os.path.join(os.path.dirname(__file__), 'fixtures', *args)
