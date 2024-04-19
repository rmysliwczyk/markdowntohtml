# markdowntohtml
This python library will convert markdown to HTML.

## Usage
```
import markdowntohtml

html = markdowntohtml.convert("markdown goes here")
```

## Tests
test_markdowntohtml.py file contains a unit test for `pytest`.  
This test will compare the output of my library to [markdown2](https://github.com/trentm/python-markdown2) converter.  
Be advised, failed test does not have to mean the error in conversion.  My library might provide a slighltly different output, which will still be a valid HTML. On failed test, please compare the output that will be printed.
