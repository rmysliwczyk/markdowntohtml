import markdowntohtml
import markdown2
import pytest
import sys

# Compares the output of my converter to markdown2 (a popular md converter)
def test_convert():
        with open("Test.md","r") as f:
            input_string = f.read()
            print(input_string)
        print("--- markdowntohtml (Failed test does not neceserilly mean wrong conversion. Please compare outputs)")
        result_from_mdtohtml = markdowntohtml.convert(input_string)
        print(result_from_mdtohtml)
        print("-------------------- markdown2")
        result_from_markdown2 = markdown2.markdown(input_string)
        print(result_from_markdown2)
        print("------------------------------")
        assert result_from_mdtohtml == result_from_markdown2
