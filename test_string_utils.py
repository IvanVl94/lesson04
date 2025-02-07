import pytest
from StringUtils import string_utils

class TestStringUtils:
    # Позитивные тесты
    
    
    def test_to_uppercase(self):
        assert string_utils.to_uppercase("test") == "TEST"
        assert string_utils.to_uppercase("123") == "123"
        assert string_utils.to_uppercase("04 апреля 2023") == "04 АПРЕЛЯ 2023"

    def test_to_lowercase(self):
        assert string_utils.to_lowercase("TEST") == "test"
        assert string_utils.to_lowercase("123") == "123"
        assert string_utils.to_lowercase("04 апреля 2023") == "04 апреля 2023"

    def test_capitalize(self):
        assert string_utils.capitalize("test") == "Test"
        assert string_utils.capitalize("tESt") == "Test"
        assert string_utils.capitalize("  test") == "  test"

    def test_reverse(self):
        assert string_utils.reverse("test") == "tset"
        assert string_utils.reverse("123") == "321"
        assert string_utils.reverse("04 апреля 2023") == "3202 ялрепа 40"
    
    # Негативные тесты
    
    def test_to_uppercase_empty(self):
        assert string_utils.to_uppercase("") == ""

    def test_to_lowercase_empty(self):
        assert string_utils.to_lowercase("") == ""

    def test_capitalize_empty(self):
        assert string_utils.capitalize("") == ""

    def test_reverse_empty(self):
        assert string_utils.reverse("") == ""

    def test_to_uppercase_spaces(self):
        assert string_utils.to_uppercase(" ") == " "

    def test_to_lowercase_spaces(self):
        assert string_utils.to_lowercase(" ") == " "

    def test_capitalize_spaces(self):
        assert string_utils.capitalize(" ") == " "

    def test_reverse_spaces(self): 
        assert string_utils.reverse(" ") == " "

    def test_to_uppercase_none(self):
        assert string_utils.to_uppercase(None) is None

    def test_to_lowercase_none(self):
        assert string_utils.to_lowercase(None) is None

    def test_capitalize_none(self):
        assert string_utils.capitalize(None) is None

    def test_reverse_none(self):
        assert string_utils.reverse(None) is None