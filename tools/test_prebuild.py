#!/bin/python3

"""Test prebuild."""

import StringIO
import sys

import prebuild

mdfile = "tools/example.md"
htmlfile = "tools/example.html"


samplemd = """# Heading 1
This is some text

## Heading 2
This is some more text.
This is an *emphasized* word.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

```
What about code blocks?
```
"""

samplehtml = """<h1>Heading 1</h1>
<p>This is some text</p>
<h2>Heading 2</h2>
<p>This is some more text.
This is an <em>emphasized</em> word.</p>
<table>
<thead>
<tr>
<th>Tables</th>
<th align="center">Are</th>
<th align="right">Cool</th>
</tr>
</thead>
<tbody>
<tr>
<td>col 3 is</td>
<td align="center">right-aligned</td>
<td align="right">$1600</td>
</tr>
<tr>
<td>col 2 is</td>
<td align="center">centered</td>
<td align="right">$12</td>
</tr>
<tr>
<td>zebra stripes</td>
<td align="center">are neat</td>
<td align="right">$1</td>
</tr>
</tbody>
</table>
<p><code>What about code blocks?</code></p>"""


def test_directmkdown():
    """Test directmkdown."""
    old_stdout = sys.stdout
    capturer = StringIO.StringIO()
    sys.stdout = capturer
    # call functions
    prebuild.directmkdown(mdfile)
    # end functions
    sys.stdout = old_stdout
    output = capturer.getvalue()
    assert output == samplehtml


def test_mkdown():
    """Test mdown."""
    assert prebuild.mkdown(samplemd) == samplehtml


def test_source():
    """Test source."""
    assert prebuild.source(mdfile) == samplemd


def test_output():
    """Test output."""
    assert prebuild.output(htmlfile, "</p>") is True


if __name__ == '__main__':
    pass
