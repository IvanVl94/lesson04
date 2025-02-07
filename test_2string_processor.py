import pytest
from string_processor import StringProcessor

class TestStringProcessor:
    def test_process_positive_case_1(self):
        assert StringProcessor.process("hello") == "Hello."

    def test_process_positive_case_2(self):
        assert StringProcessor.process("this is a test") == "This is a test."

    def test_process_positive_case_3(self):
        assert StringProcessor.process("end") == "End."

    def test_process_negative_case_1(self):
        assert StringProcessor.process("") == "."

    def test_process_negative_case_2(self):
        assert StringProcessor.process("no ending") == "No ending."