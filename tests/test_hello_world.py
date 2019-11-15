from unittest import TestCase
from unittest.mock import patch

from tmp_great_app.tmp_hello_world import hello_world


@patch('builtins.print')
class TestStringMethods(TestCase):
    def test_hello_world__called_once(self, print_mock):
        hello_world()
        print_mock.assert_called_once()

    def test_hello_world__called_with(self, print_mock):
        hello_world()
        print_mock.assert_called_with('Hello World!')

    def test_hello_world__called_once_with(self, print_mock):
        hello_world()
        print_mock.assert_called_once_with('Hello World!')
